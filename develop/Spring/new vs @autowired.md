# New Keyword VS @autowired



새로 접근할 때 작동 방식이 다름.

@autowired -> singleton 방식

Autowired는 이미 생성된 객체(Spring Bean)를 주입받겠다는 애노테이션이지 객체를 생성하라는 애노테이션이 아닙니다.



new로 생성할 때 객체가 내부에서 다른 스프링빈들을 참조하고있을경우 new로 생성하게되면 그 빈들을 주입받지 못합니다.

https://jeong-pro.tistory.com/174

