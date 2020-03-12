# Spring Boot Bean 생성 순서관련 자료

스프링/스프링부트에서 bean을 등록하는 방법은 여러가지가 있다.

스프링부트에서는 Bean을 등록할 때 자바코드(Annotation)로 등록하는 것을 권장한다.

따라서 스프링 부트를 사용하는 개발자들은 @Component, @Service, @Controller, @Repository, @Bean, @Configuration 등으로 Bean들을 등록하고 주입받아 사용하는게 일반적이다.

그런데 프로그램 개발중에 아무 생각없이 여러 개의 Bean들을 등록해놓고 어떤 Bean에서 @Autowired로 자연스럽게 주입받아서 '사용'하려다가 에러를 만났다.

바로 Bean에 **'아직'** 등록되지 않은 Bean을 클래스에서 사용하려고 했기 때문이다.

무슨 얘기인지 Spring을 기준으로 설명하겠다. (Spring boot랑은 조금 다름.)

A라는 클래스에서 @Component를 사용해서 bean이 자동적으로 등록되기를 원하고, B라는 클래스도 @Component를 사용해서 bean이 자동적으로 등록되기를 원하는 상황일 때,

B라는 클래스 내부에서는 A라는 클래스의 인스턴스(Bean)를 @Autowired로 주입받아서 해당 인스턴스의 method를 이용하려는 흐름이다.

사실 모든 bean들이 알아서 뜰때까지 무언가 작업을 하지 않으면 문제가 없을 수 있으나 bean이 생성되자마자 초기화같은 어떤 작업을 해버린다면 얘기가 달라진다.

참고로 Spring에서 xml을 이용해서 bean을 등록하게되면 자동적으로 위에서 아래로 bean들을 스캔하여 생성한다.

그런데 bean 생성 순서가 바뀌어야하는 상황이라면 어떨까?

아주 좋게도 스프링이 알아서 순서를 바꿔서 참조되는 bean(예시에서 A)을 먼저 생성하고 참조하고 있는 bean(예시에서 B)를 나중에 생성한다.

그래서 스프링에서는 문제가 되지 않는다.

근데 스프링부트에서는 Annotation을 이용해서 bean을 등록하게되면 웃기게도(?) 패키지에서 존재하는 순서대로(위에서 아래) 스캔하면서 bean을 생성한다.

따라서 괜히 알파벳순서에서 밀린 패키지, 클래스는 생성 순서를 맞춰주지 않는 문제가 생긴다.

> **문제 상황 재현**

![img](https://t1.daumcdn.net/cfile/tistory/99422B4A5B97C24802)

현재 상황을 설명하면,

패키지 구조가 왼쪽 상단과 같이 되어있고 BeanTest1,2,3을 생성하고 오른쪽 상단과 같은 코드를 만들었다.

코드 내용은 @Component를 통해 Bean으로 등록하고 생성자에서 hello()라는 메소드로 자신이 생성되었음을 console로 찍었다.

역시나 위에서 아래로 생성되는 것을 로그를 통해 알 수 있다.

그렇다면 문제의 상황을 만들기 위해서 어떻게 해야할까?

바로 BeanTest1 클래스에서 BeanTest3 bean을 주입받아 hello()메소드를 호출해 보는 방법으로 재현할 것이다.

```java
package com.example.demo.beans;
 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
 
@Component
public class BeanTest1 {
    
    @Autowired
    BeanTest3 beanTest3;
    
    public  BeanTest1() {
        hello();
        beanTest3.hello();
    }
    public void hello() {
        System.out.println("hello Bean1");
    }
}

```



![img](https://t1.daumcdn.net/cfile/tistory/99C2784E5B97C3A226)

결과는 위 그림과 같이 BeanCreationException을 발생시킨다. (hello Bean1은 찍히고 있음을 확인, hello Bean2,3는 안보임)

Bean3가 생성되지도 않았는데 주입받았을 것이라 생각하고 사용해버리니까 에러가 난 것이다.

이 문제를 해결하는 방법은 여러가지가 있다. 다 해볼 것이다.

> **Bean 순서 결정법 1**

**@DependsOn 애노테이션을 사용하자**

결국은 스프링한테 "이 빈(Bean)은 어떤 X라는 빈을 참조하고 있어(의존하고 있어)" 라고 알려주는 것과 같다.

```java
package com.example.demo.beans;
 
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
 
@Configuration
public class BeanTest3 {
    public BeanTest3() {
        System.out.println("Beantest3 생성");
    }
    
    @Bean("Bean3")
    public BeanTest3 create() {
        return this;
    }
    public void hello() {
        System.out.println("hello Bean3");
    }
}
```

[BeanTest3.class]

```java
package com.example.demo.beans;
 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.DependsOn;
import org.springframework.stereotype.Component;
 
@Component
@DependsOn(value = {"Bean3"})
public class BeanTest1 {
    
    @Autowired
    BeanTest3 beanTest3;
    
    public  BeanTest1() { 
        //hello(); 이렇게하면 생성하면서 마찬가지로 주입받은 빈을 바로 사용하는 것과 같기 때문에 에러남
        System.out.println("BeanTest1 생성");
    } 
    
    public void hello() {
        beanTest3.hello();
        System.out.println("hello Bean1");
    }
}
```

[BeanTest1.class]

위 코드에서 보다시피 클래스에 @DependsOn이라는 애노테이션을 쓰고 Bean3로 등록되는 bean에 의존하고 있다는 것을 알려주었다.

참고로 @Component("Bean3") 이런식으로 빈을 등록해봤을 때는 에러가 발생했다.

그래서 @Configuration에 @Bean으로 등록하는 방식으로 등록했더니 잘 참고해서 아래와 같은 결과를 얻을 수 있었다. (생성 순서, 엄밀히 말하면 이것으로 인증할 순 없음.)

![img](https://t1.daumcdn.net/cfile/tistory/99F613415B99003403)

\* 요약

결과적으로 @DependsOn을 사용하면 의존한다는 사실을 스프링에게 직접 알려줄 수 있어서 문제는 해결된다.

하지만 이런식으로 코드를 여러 곳에 작성하면 다른 사람이 코드를 봤을 때 헷갈릴 수도 있다.

또한 여러 곳에 작성하다보면 무한루프(?)가 걸릴 수 있다. A->B->C->A 이런식으로 의존이 고리를 형성해버릴 수 있다.

그리고 @Component("Bean3") 이런식으로 코드 작성이 불가한게 단점이다. (사실 아닐 수 있음, 테스트에서는 안됨.)

> **Bean 순서 결정법 2**

**@PostConstruct 애노테이션을 사용하자**

위의 애노테이션은 해당 컴포넌트가 완전히 생성된 후(주입된 후)에 한 번 실행해야할 일들을 코딩한 메소드에 붙이는 것이다.

즉, 해당 Bean이 완전히 생성된 후 무언가 작동하므로 NullPointerException이 일어나지 않는다.

물론 생성자에 붙이는 것은 여지없이 에러가 난다.

```java
@Component
public class BeanTest1 {
    
    @Autowired
    BeanTest3 beanTest3;
    
    public  BeanTest1() { 
        System.out.println("BeanTest1 생성");
    }  
    
    @PostConstruct
    public void hello() {
        beanTest3.hello();
        System.out.println("hello Bean1");
    }
}
```

[BeanTest1.class]



```java
@Component
public class BeanTest3 {
    public BeanTest3() {
        System.out.println("Beantest3 생성");
    }
    
    public void hello() {
        System.out.println("hello Bean3");
    }
}
```

[BeanTest3.class]

위와 같이 beanTest3.hello();가 빈이 완전히 생성된(@Autowired로 주입까지 완료된) 상태에서 실행되다보니 에러가 해결된다.

\* 참고로 이 방법이 다른 빈들에게 의존성을 부여하지도 않고 깔끔한 코드가 되기 때문에 **가장 적절한 방법**이다.



> **Bean 순서 결정법 3**

**@Order 는 뭘까?**

문제와는 약간 다르지만 특별한 상황에서 Bean 생성 순서를 결정할 수 있는? 방법이 @Order다.

간단하게 소개하면 같은 인터페이스를 구현하는 여러 Bean들이 어느 한 객체로 주입될 때 순서를 정할 수 있는 것이다.

```java
public interface Person {
    public void eat();
}
 
=========================================
@Component
@Order(2)
public class Jeongpro implements Person {
    @Override
    public void eat() {
        System.out.println("jeongpro");
    }
}
=========================================
@Component
@Order(1)
public class Tistory implements Person {
    @Override
    public void eat() {
        System.out.println("tistory");
    }
}
=========================================
@Component
public class BeanTest1 {
    
    @Autowired
    List<Person> people;
    
    public  BeanTest1() { 
        System.out.println("BeanTest1 생성");
    }  
    
    @PostConstruct
    public void hello() {
        people.stream().forEach(x->x.eat());
    }
}
```



Person이라는 인터페이스를 구현하고 있는 객체들이 BeanTest1에서 List<Person> people; 이라는 객체에 주입될 때 들어가는 순서를 정하는 것이다. @Order의 순서대로 제일앞에는 Tistory가 들어가고 다음에 Jeongpro가 들어간다.

![img](https://t1.daumcdn.net/cfile/tistory/99589C415B9907071E)

[결과]

\* 또 다른 방법으로 Bean이 주입되지 않았을 때를 고려해서 생성자에서 해당 bean을 파라미터로 받는 방법인데 마찬가지로 의존성을 단적으로 보여줘버리기 때문에 지양한다.



https://jeong-pro.tistory.com/167
출처:  [기본기를 쌓는 정아마추어 코딩블로그]



