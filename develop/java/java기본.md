# Static keyword
1.클래스를 설계할 때, 멤버변수 중 모든 인스턴스에 공통적으로 사용해야하는 것에 static을 붙인다.
 - 인스턴스를 생성하면, 각 인스턴스들은 서로 독립적기 때문에 서로 다른 값을 유지한다. 경우에 따라서는 각 인스턴스들이 공통적으로 같은 값이 유지되어야 하는 경우 static을 붙인다.

2. static이 붙은 멤버변수는 인스턴스를 생성하지 않아도 사용할 수 있다.
 - static이 붙은 멤버변수(클래스변수)는 클래스가 메모리에 올라갈때 이미 자동적으로 생성되기 때문이다.

3. static이 붙은 메서드(함수)에서는 인스턴스 변수를 사용할 수 없다.
 - static이 메서드는 인스턴스 생성 없이 호출가능한 반면, 인스턴스 변수는 인스턴스를 생성해야만 존재하기 때문에... static이 붙은 메서드(클래스메서드)를 호출할 때 인스턴스가 생성되어있을수도 그렇지 않을 수도 있어서 static이 붙은 메서드에서 인스턴스변수의 사용을 허용하지 않는다. (반대로, 인스턴스변수나 인스턴스메서드에서는 static이 붙은 멤버들을 사용하는 것이 언제나 가능하다. 인스턴스변수가 존재한다는 것은 static이 붙은 변수가 이미 메모리에 존재한다는 것을 의미하기 때문이다.)

4. 메서드 내에서 인스턴스 변수를 사용하지 않는다면, static을 붙이는 것을 고려한다.
 - 메서드의 작업내용중에서 인스턴스 변수를 필요로 한다면, static을 붙일 수 없다. 반대로 인스턴스변수를 필요로 하지 않는다면, 가능하면 static을 붙이는 것이 좋다. 메서드 호출시간이 짧아지기 때문에 효율이 높아진다. (static을 안붙인 메서드는 실행시 호출되어야할 메서드를 찾는 과정이 추가적으로 필요하기 때문에 시간이 더 걸린다.)


5. 클래스 설계시 static의 사용지침
 - 먼저 클래스의 멤버변수중 모든 인스턴스에 공통된 값을 유지해야하는 것이 있는지 살펴보고 있으면, static을 붙여준다.
 - 작성한 메서드 중에서 인스턴스 변수를 사용하지 않는 메서드에 대해서 static을 붙일 것을 고려한다.

 
일반적으로 인스턴스변수와 관련된 작업을 하는 메서드는 인스턴스메서드(static이 안붙은 메서드)이고 static변수(클래스변수)와 관련된 작업을 하는 메서드는 클래스메서드static이 붙은 메서드)라고 보면 된다.

# Interface , default
Interface
- 완벽한 추상화를 달성하기 위해서 사용
- 인터페이스를 사용함으로써 다중상속
- 인터페이스의 사용은 약한 결합
- 다형성

default method
인터페이스는 기능에 대한 선언만 가능하기 때문에, 실제 코드를 구현한 로직은 포함될 수 없습니다. 하지만 자바8에서 이러한 룰을 깨트리는 기능이 나오게 되었는 데, 그것이 Default Method(디펄트 메소드)입니다. 메소드 선언시에 default를 명시하게 되면 인터페이스 내부에서도 코드가 포함된 메소드를 선언 할 수 있습니다. (접근제어자에서 사용하는 default와 같은 키워드 이지만, 접근제어자는 아무것도 명시 하지 않은 접근 제어자를 default라고 하며 인터페이스의 default method는 'default'라는 키워드를 명시해야 합니다.)

# unchecked , checked exception 어떻게 강제로 만드는지
- unchecked Exception
  - runtime exception을 상속함
  - 명시적인 예외 처리를 강제하지 않음
  - runtime Exception 발생 시 롤백함
  - ex) NullPointerException
- checked Exception
  - 명시적으로 처리해야함 try Catch / throw 로 던져야함
  - roll back 안함 : 기본적으로 Checked Exception는 복구가 가능하다는 메커니즘을 가지고 있다. 예를 들어서 특정 이미지 파일을 찾아서 전송해주는 함수에서 이미지를 찾지 못했을 경우 기본 이미지를 전송한다. `복구 전략`을 가질 수 있게 된다.
  - ex) SQLException
- 
  Checked Exception을 만나면 더 `구체적인 Unchecked Exception`을 발생시켜 정확한 정보를 전달하고 로직의 흐름을 끊어야 합니다.

# comparable 자바 
Comparable, Comparator하면 '정렬'을 떠올려야하는 것이다.

Comparable : 객체 간의 일반적인 정렬이 필요할 때, Comparable 인터페이스를 확장해서 정렬의 기준을 정의하는 compareTo() 메서드를 구현한다.
현재 객체 < 파라미터로 넘어온 객체: 음수 리턴
현재 객체 == 파라미터로 넘어온 객체: 0 리턴
현재 객체 > 파라미터로 넘어온 객체: 양수 리턴

Comparator : 객체 간의 특정한 정렬이 필요할 때, Comparator 인터페이스를 확장해서 특정 기준을 정의하는 compare() 메서드를 구현한다.
정렬 가능한 클래스(Comparable 인터페이스를 구현한 클래스)들의 기본 정렬 기준과 다르게 정렬 하고 싶을 때 사용하는 인터페이스
package: java.util.Comparator
주로 익명 클래스로 사용된다.
기본적인 정렬 방법인 오름차순 정렬을 내림차순으로 정렬할 때 많이 사용한다

# ConcurrentHashMap , Thread Safe
동기화(Synchronize)라고 표현하기도 하며 어떠한 Class의 인스턴스가 여러개의 Thread에서 동시 참조되고 해당 객체에 Operation 이 발생해도 정합성을 유지해줄때 보통 우리는 Thread-Safe 하다 라고 표현한다.  @ThreadSafe 어노테이션을 이용해 해당 Class가 Thread-Safe 함을 표시하기도 한다.   어떠한 경우에도 개발자가 의도한대로 정확하게 동작한다라고도 이야기 할 수 있다.  참조하는(사용하는) 쪽에서 특별한 동기화 없이도 정확히 동작한다는 것을 이야기한다.  멀티 Thread 환경에서는 필수 적인 요소이다.  Java에서 Thread-Safe 를 이루는 방향 및 조건은 여러 가지가 있으나 이번 Post에는 따로 소개하지는 않는다.

검색과 갱신 전체에 걸쳐 Thread-Safe 함을 보장하면서도 높은 성능을 보장하는 HashMap 이다.  HashMap처럼 기본적으로는 Hashtable 과 동일한 Spec을 제공한다.   Hashtable 또한 Thread-Safe를 보장한다. 그러나 차이점은 모든 작업이 Thread-Safe 임에도 불구하고 검색작업(get과 같은)에는 Lock이 수반되지 않으며, 전체 테이블을 잠궈야 하는 액션도 없다.  
  ConcurrentHashMap의 검색 작업(get 포함)은 Lock이 이루어지지 않으며 갱신 작업(put 및 remove 포함)과 동시에 수행 될 수 있다.  반대로 Hashtable 의 내부 코드를 살펴보면 Thread-Safe를 보장하는 방법으로 put, get 등의 검색 및 갱신 작업의 method 레벨에서 synchronized 키워드를 사용한다.  이는 간편하게 동시접근을 막아 Thread-safe 를 보장하는 방법 중 하나이다.  그러나 method 레벨에서 synchronized 키워드를 이용하면 Lock의 매개로 활용객체가 바로 객체바로 자신이 된다(this).  이는 전체적인 성능 저하를 가져온다.  어느 한 순간에 Lock이 설정된 어떤 method도 하나의 Thread만이 진입할 수 가 있게 된다. (누군가 get으로 Lock을 획득 중이면, put도 진입할 수가 없다.)

 ConcurrentHashMap의 검색은 검색 method가 실행되는 시점에 가장 최근에 완료된 갱신 작업의 결과를 반영한다.  putAll 및 clear와 같은 집계 작업의 경우 동시 검색에는 해당 시점에 put / remove 중인 일부 항목만 반영될 수 있다.  마찬가지로, iterator, Spliterator, Enumeration 수집 생성 시점 또는 이후 어느 한 시점의 상태를 반영하는 요소를 반환한다.  Hashtable에서 활용되던 ConcurrentModificationException은 이제 더이상 사용되지 않는다.  

 # Syncronized / Critical session
 자바 코드에서 동기화 영역은 synchronizred 키워드로 표시된다. 동기화는 객체에 대한 동기화로 이루어지는데(synchronized on some object), 같은 객체에 대한 모든 동기화 블록은 한 시점에 오직 한 쓰레드만이 블록 안으로 접근하도록 - 실행하도록 - 한다. 블록에 접근을 시도하는 다른 쓰레드들은 블록 안의 쓰레드가 실행을 마치고 블록을 벗어날 때까지 블록(blocked) 상태가 된다.

synchronized 키워드는 다음 네 가지 유형의 블록에 쓰인다.

인스턴스 메소드
스태틱 메소드
인스턴스 메소드 코드블록
스태틱 메소드 코드블록

어떤 동기화 블록이 필요한지는 구체적인 상황에 따라 달라진다.

- 인스턴스 메소드 동기화

다음은 동기화 처리된 인스턴스 메소드이다.

public synchronized void add(int value){
      this.count += value;
  }

메소드 선언문의 synchronized 키워드를 보자. 이 키워드의 존재가 이 메소드의 동기화를 의미한다.

인스턴스 메소드의 동기화는 이 메소드를 가진 인스턴스(객체)를 기준으로 이루어진다. 그러므로, 한 클래스가 동기화된 인스턴스 메소드를 가진다면, 여기서 동기화는 이 클래스의 한 인스턴스를 기준으로 이루어진다. 그리고 한 시점에 오직 하나의 쓰레드만이 동기화된 인스턴스 메소드를 실행할 수 있다. 결국, 만일 둘 이상의 인스턴스가 있다면, 한 시점에, 한 인스턴스에, 한 쓰레드만 이 메소드를 실행할 수 있다. 

인스턴스 당 한 쓰레드이다. 

- 스태틱 메소드 동기화

스태틱 메소드의 동기화는 인스턴스 메소드와 같은 방식으로 이루어진다.

  public static synchronized void add(int value){
      count += value;
  }
역시 선언문의 synchronized 키워드가 이 메소드의 동기화를 의미한다.

스태틱 메소드 동기화는 이 메소드를 가진 클래스의 클래스 객체를 기준으로 이루어진다. JVM 안에 클래스 객체는 클래스 당 하나만 존재할 수 있으므로, 같은 클래스에 대해서는 오직 한 쓰레드만 동기화된 스태틱 메소드를 실행할 수 있다.

만일 동기화된 스태틱 메소드가 다른 클래스에 각각 존재한다면, 쓰레드는 각 클래스의 메소드를 실행할 수 있다.

클래스 -쓰레드가 어떤 스태틱 메소드를 실행했든 상관없이- 당 한 쓰레드이다.

인스턴스 메소드 안의 동기화 블록

동기화가 반드시 메소드 전체에 대해 이루어져야 하는 것은 아니다. 종종 메소드의 특정 부분에 대해서만 동기화하는 편이 효율적인 경우가 있다. 이럴 때는 메소드 안에 동기화 블록을 만들 수 있다.

  public void add(int value){

    synchronized(this){
       this.count += value;   
    }
  }

이렇게 메소드 안에 동기화 블록을 따로 작성할 수 있다. 메소드 안에서도 이 블록 안의 코드만 동기화하지만, 이 예제에서는 메소드 안의 동기화 블록 밖에 어떤 다른 코드가 존재하지 않으므로, 동기화 블록은 메소드 선언부에 synchronized 를 사용한 것과 같은 기능을 한다.

동기화 블록이 괄호 안에 한 객체를 전달받고 있음에 주목하자. 예제에서는 'this' 가 사용되었다. 이는 이 add() 메소드가 호출된 객체를 의미한다. 이 동기화 블록 안에 전달된 객체를 모니터 객체(a monitor object) 라 한다. 이 코드는 이 모니터 객체를 기준으로 동기화가 이루어짐을 나타내고 있다. 동기화된 인스턴스 메소드는 자신(메소드)을 내부에 가지고 있는 객체를 모니터 객체로 사용한다.

같은 모니터 객체를 기준으로 동기화된 블록 안의 코드를 오직 한 쓰레드만이 실행할 수 있다.


다음 예제의 동기화는 동일한 기능을 수행한다.

  public class MyClass {
  
    public synchronized void log1(String msg1, String msg2){
       log.writeln(msg1);
       log.writeln(msg2);
    }

  
    public void log2(String msg1, String msg2){
       synchronized(this){
          log.writeln(msg1);
          log.writeln(msg2);
       }
    }
  }

한 쓰레드는 한 시점에 두 동기화된 코드 중 하나만을 실행할 수 있다. 여기서 두 번째 동기화 블록의 괄호에 this 대신 다른 객체를 전달한다면, 쓰레드는 한 시점에 각 메소드를 실행할 수 있다. -동기화 기준이 달라지므로.

- 스태틱 메소드 안의 동기화 블록

다음 예제는 스태틱 메소드에 대한 것이다. 두 메소드는 각 메소드를 가지고 있는 클래스 객체를 동기화 기준으로 잡는다.

  public class MyClass {

    public static synchronized void log1(String msg1, String msg2){
       log.writeln(msg1);
       log.writeln(msg2);
    }

  
    public static void log2(String msg1, String msg2){
       synchronized(MyClass.class){
          log.writeln(msg1);
          log.writeln(msg2);  
       }
    }
  }

같은 시점에 오직 한 쓰레드만 이 두 메소드 중 어느 쪽이든 실행 가능하다. 두 번째 동기화 블록의 괄호에 MyClass.class 가 아닌 다른 객체를 전달한다면, 쓰레드는 동시에 각 메소드를 실행할 수 있다.

- 자바 컨커런시 유틸리티

synchronized 매카니즘은 다수의 쓰레드에게 공유되는 객체로의 접근에 대한 자바의 첫 번째 동기화 매카니즘이었다. 이 매카니즘이 아주 훌륭하지는 못했기 때문에, 이보다 한층 나은 동시성 컨트롤을 위해 자바 5 에서는 컨커런시 유틸리티 클래스들이 출현하게 된다.


# pojo 클래스를 만들때 무조건 쓰는 방법?

# daum.net 입력했을 때 뒤에서 어떤 상황이 발생하는지

# get, post 형식 json body

# option method
요청 전 어떤 응답이 가능한지 알려주는 메소드

# spring DI

# js this
실행문맥이란 말은 호출자가 누구냐는 것과 같습니다.

# git rebase


# JVM 메모리 구조
- method area : 클래스 정보, 클래스 변수
- heap : 인스턴스
- stack : 메서드의 작업에 필요한 메모리 공간

# super() 조상 클래스의 생성자
상속을 받은 하위 클래스에 생성자를 지정할 때 컴파일러가 상위 클래스의 생성자를 호출하는 `super();`가 없다면 자동으로 작성한다.
여기서, 만약 조상 클래스의 생성자가 매개변수를 받는 생성자이면 하위클래스에서 오류가 발생한다.

```java
// 이 클래스에서는 생성자가 메소드를 받는 생성자를 생성하였음으로 자동으로 아무 매소드를 받지 않는 생성자는 생성되지 않는다!!

class Point {
  int x, y;
  Point(int x, int y) {
    this.x = x;
    this.y = y;  
  }
}

// 이 경우 컴파일러에서 Point3D 생성자 첫줄에 super(); 를 삽입한다.
class Point3D extends Point{
  int x,y,x;
  Point3D(int x, int y int z) {
    //super();
    // super를 삽입하면 Point 클래스에는 생성자가 없기 떄문에 오류 발생
    this.x = x;
    this.y = y;
    this.z = z;
  }
}

// 정상적으로 동작시키기 위해서는 super를 정확히 입력해준다.
class Point3D extends Point{
  int x,y,x;
  Point3D(int x, int y int z) {
    super(x,y);
    this.z = z;
  }
}
```
이렇게 오류가 발생하는 이유는 생성자를 생성할 때 부모클래스를 참조할 수 있기 때문에 그 전에 초기화 해줘야 하기 때문이다.


# 상속
- 기존의 클래스를 재사용하여 새로운 클래스를 작성
- 생성자와 초기화 블럭은 상속되지 않는다. 멤버만 상속됨
- 자손 클래스의 맴버 개수 >= 부모 클래스의 멤버 개수

## 포함관계
- 클래스의 멤버변수로 다른 클래스를 사용하는것

**상속은 "a는 b이다." 포함은 "a는 b를 가지고 있다" **

## 단일 상속의 장점
클래스간의 관계가 덜 복잡해진다.
다중 상속의 경우 부모 클래스의 멤버간의 이름이 같은 경우 구별할 수 없다.

# 오버라이딩
- 조상 클래스로부터 상속 받은 메서드의 내용을 변경하는 것
## 조건
1. 이름이 같아야 한다.
2. 매개변수가 같아야 한다.
3. 반환 타입이 같아야 한다.
4. 접근 제어자는 조상 클래싀이 메서드보다 좁은 범위로 변경할 수 없다.
  - 접근 제어자 순서 public > protected > (default) > private
5. 조상 클래스의 메서드보다 많은 수의 예외를 선언할 수 없다.
  - 단 예외의 개수가 아니라 선언 된 예외가 얼마나 많은 예외를 던질 수 있는지
6. 인스턴스메서드가  static이 될 수 없으며 반대도 될 수 없다.
  - static은 어차피 특정 클래스에 존재하는 친구이다.

# 오버로딩
같은 매서드에 다른 인자값을 통해 같은 메서드 네임의 함수를 만드는것


# package / import
1. package 는 물리적으로 하나의 디렉토리
  - 하나의 소스 파일에는 첫 번째 문장으로 단 한 번의 패키지 선언만을 허용
  - 모든 클래스는 반드시 하나의 패키지에 속해야 한다.
  - 패키지는 점(.)을 구분자로 하여 계층구조로 구성할 수 있다.
  - 패키지는 물리적으로 클래스 파일을 포함하는 하나의 디렉토리이다.

2. package 선언
  - 소스 파일의 맨 위에 `pacakge 패키지명;`으로 선언한다.
  - 모든 클래스는 반드시 패키지에 속해야한다. 하지만, 패키지를 선언하지 않아도 동작되는 이유는 `unnamed package`때문이다.

3. import
  - 모든 소스 파일에서 import문은 pacakge 문 다음에 클래스 선언문 이전에 위치해야한다.
  - 많은 import문을 쓸 수 있다.
  - import 패키지명.클래스명; vs import 패키지명.*; -> 성능 차이가 없다. : 컴파일 될때 컴파일러가 찾는것일뿐

  - static import 문
    static import 문을 사용하면 static 멤버를 호출할 때 클래스 이름을 생략할 수 있다.
    ```java
    import static java.lang.Math.random;
    log.info(random());
    ```

# 제어자
1. 클래스, 변수 또는 메서드의 선언부에 함께 사용되어 부가적인 의미를 부여한다.
  - 접근 제어자 : public, protected, default, private
  - 그 외 : static, final, abstract, native, transient, synchronized, volatile, strictfp

2. static
  - 인스턴스 변수는 클래스로부터 생성되어도 각각 인스턴스 마다 각기 다른 값을 유지함
  - class변수는 인스턴스에 상관 없이 같은 값을 갖는다.
  - 멤버변수, 메서드, static 초기화 블럭
  - 클래스가 로드될때 method area에 생성된다.
  - 인스턴스가 생성 되지않아도 사용가능하다.

3. final
  - 변수에 사용되면 값을 변경할 수 없는 상수
  - 메서드에 사용되면 오버라이딩을 할 수 없게 되고 클래스에 사요되면 자손클래스 정의 불가.
  - 클래스, 메서드, 멤버변수, 지역변수
  - 인스턴스 변수는 생성자를 통해 초기화 가능

4. abstract
  - 메서드의 선언부만 작성함 추상 메서드
  - 클레스, 메서드에서 사용가능
  - 인스턴스 생성 불가

5. 접근 제어자
  - 클래스, 멤버면수, 메서드, 생성자 사용가능
  1. private 같은 클래스 내에서만 접근 가능
  2. default 같은 패키지내에서만 접근가능
  3. protected 같은 패키지 및 상속 받은 클래스에서 접근가능
  4. public 모두 접근가능

  - 접근 제어자를 이용한 캡슐화
    - 외부로부터 데이터를 보호하기 위해서
    - 외부에는 불필요한 내부적으로만 사용되는 부분을 감추기 위해서
  
  public 메서드를 변경하면 이 메서드들을 사용하는 모든 곳을 테스트 해야함

  - 생성자의 접근 제어자
    - 생성자의 접근 제어자를 private 로 하면 외부에서 생성자에 접근할 수 없다.
    - 결국 인스턴스 생성이 불가능 하다.


# Final
final 키워드는 엔티티를 한 번만 할당합니다. 즉, 두 번 이상 할당하려 할 때 컴파일 오류가 발생하여 확인이 가능합니다.
결국 Java에서의 final은 Immutable/Read-only 속성을 선언하는 지시어입니다.
클래스, 함수, 변수가 변하지 못하도록 의도하고 싶다면 final로 선언하자.

# Singleton 패턴 getInstance
- 생성자를 통해 직접 인스턴스를 생성하지 못하게 하고 public 메서드를 통해 인스턴스에 접근하게 함으로써 사용할 수 있는 `인스턴스의 개수`를 제한할 수 있다.
- 생성자가 `private`인 클래스는 다른 클래스의 조상이 될 수 없다.
이유는 자손 클래스가 생성할때 부모 클래스의 생성자를 호출해야되는데 불가능하기 때문이다.
-> 결국 이렇게 사용할 경우 클래스 앞에 final을 붙여주는게 좋다.

- singleton 패턴
**프로그램내에서 단 하나의 객체만을 생성하게 강제** 하는 패턴
  ex) 안드로이드 어플리케이션에서 하나의 사용자를 계속해서 유지할때
```java
class Singleton{

	private Singleton(){

	}

	public static Singleton getInstance(){
		return new Singleton(); //getInstance를 호출 할 때마다 계속 새로운 객체가 생성이됨 !!

	}

}

public class SingletonTest {

	public static void main(String[] args) {

		Singleton single = Singleton.getInstance();

	}

}

```
이러면 호출 할때마다 계속 생성할 수 있다.
```java
class Singleton{

	private static Singleton one;

	private Singleton(){	

	}

	

	public static Singleton getInstance(){

		if (one == null){

			one = new Singleton();

		}

		return one;

	}

}

```
getInstance가 최초로 불려지면 Singleton객체 one은 new에 의해서 객체가 생성이 되고, 

one 은 static변수 이기 때문에 그 이후로는 null이 아니고 이미 만들어진 객체 이므로 항상 one를 리턴하게 된다.

즉, 프로그램 내에서 Singleton이라는 객체는 단 하나만 만들어지는 것이다.

** 제어자 필수 **
1. 메서드에 static 과 abstract를 함께 사용할 수 없다.
2. 클래스에 abstract와 final을 동시에 사용할 수 없다.
  - 클래스에 사용되는 final의 의미는 더이상 상속이 불가능하다는 의미인데 abstract는 상속이 되어야만 사용할 수 있기 때문이다.
3. abstract 메서드의 접근 제어자가 private일 수 없다.
  abstract 메서드는 상속받은 클래스가 구현 해야하는데 private이면 구현 할 수 없기 때문이다.
4. 메서드에 private와 final을 같이 사용할 필요는 없다.
  private만 해도 상속받을 수 없기 떄문.


# 다형성
  - 조상클래스 타입의 참조변수로 자손클래스의 인스턴스를 참조할 수 있도록 하다.
  - 같은 타입의 인스턴스지만 참조변수의 타입에 따라 사용할 수 있는 멤버의 개수가 달라진다.
  - 자손 타입의 참조변수로 조상타입의 인스턴스는 불가능 `CaptionTv c = new Tv();`
  - 조상타입의 참조변수 = 자손타입의 인스턴스 가능 `Tv c = new CaptionTv ();`
  - 자손타입은 조상타입을 완전히 대체할 수 있다.
  ## 형변환
    - 상속관계에 있는 것들끼리는 형변환 가능
    - 자손타입 -> 조상타입(Up-casting) 생략가능
    - 자손타입 <- 조상타입(Down-casting) 생략불가능
    ** 형변환은 참조변수의 타입을 변환하는것 -> 인스턴스 변환 X 그러므로 인스턴스는 그대로 **
  
  ## 참조변수와 인스턴스의 연결
    - 메서드 : 조상 클래스의 메서드를 오버라이딩한 경우 참조변수의 타입에 관계 없이 항상 실제 인스턴스(자손클래스)의 메서드가 호출
    - 멤버변수 : 참조변수의 타입에 따라 달라진다.
    ```java
    class Parent {
      int x = 100;
      void method() {
        System.out.println("parent");
      }
    }
    class Child extends Praent {
      int x = 200;
      void method() {
        System.out.println("child");
      }
    }
    Parent p = new Child();
    Child c = new CHild();

    println(p.x); // 100 참조변수의 타입이 parent
    p.method(); // child => 메서드는 인스턴스의 메서드
    println(c.x); // 200
    c.mtehod(); // child
    ```

# 추상클래스(abstract class)
  - 추상메서드를 포함한 클래스
  - 멤버변수, 생성자를 가질 수 있음
  - 인스턴스 생성은 불가능
  - 상속받은 클래스에서 추상메서드를 구현을 강요함.
  ## 추상메서드
    - `abstract 리턴타입 메서드이름();`
    - 위에 주석으로 어떤 기능을 수행할 목적으로 작성하였는지 설명하는 것이 좋음. 

# Interface
  - 인터페이스는 일종의 추상클래스이다.
  - 추상 클래스처럼 추상메서드를 가지만 일반 메서드 또는 멤버변수를 구성원으로 가질 수 없다.
  ## 제한사항
    - 모든 멤버변수는 public static final 이여야 하며 생략가능
    - 모든 메서드는 public abstract 이어야 하며 생략 가능
    - 1.8 이상부터 static 메서드와 default 메서드 사용가능
  ## 인터페이스 끼리의 상속
    - extends a, b ...
    - 다중으로 상속이 가능하다.
  ## 인터페이스의 구현
    - interface 구현은 `class 네임 implements 인터페이스이름`의 방식으로 구현한다.
    - inteface에 있는 추상메서드들을 모두 구현 하여야 한다.
    - 일부만 구현 시 abstract로 추상 클래스로 선언하여야 한다.
    - 구현한 클래스의 메서드의 접근 제어자는 `public`이다 왜냐하면 인터페이스의 모든 메서드는 `public abstract` 이기 때문이다.
  ## 인터페이스를 이용한 다형성
    - 인터페이스를 구현한 클래스 역시 조상을 인터페이스로 가질 수 있기 때문에 다형성이 가능하다.
  ** 리턴 타입이 인터페이스라는 것은 메서드가 해당 인터페이스를 구현한 클래스의 인스턴스를 반환한다는 것을 의미한다. **

  # 장점
    - 개발 시간을 단축시킬 수 있다.
      인터페이스가 작성되면 이를 사용해서 프로그램을 작성가능하다 -> 메서드를 호출하는 쪽에서 메서드의 이름만 알면 된다.
      구현하는 클래스가 구현되지 않아도 메서드를 호출하는 쪽은 개발이 가능하다.
    - 표준화가 가능하다.
      프로젝트에 사용되는 기본 틀을 인터페이스로 작성한 다음 개발자들이 구현한다면 표준화가 가능하다.
    - 서로 관계 없는 클래스들에게 관계를 맺어 줄 수 있다.
      상속관계나 조상클래스를 가지고 있지 않는 클래스들 끼리도 인터페이스를 구현하게하면 고나계 가능
    - 독립적인 프로그래밍이 가능하다.
      인터페이스를 구현한 클래스들끼리 독립적으로 동작할 수 있다.


https://martianlee.github.io/posts/naver-interview-review/
https://github.com/JaeYeopHan/Interview_Question_for_Beginner#%EB%A9%B4%EC%A0%91%EC%97%90%EC%84%9C-%EB%B0%9B%EC%95%98%EB%8D%98-%EC%A7%88%EB%AC%B8%EB%93%A4
