## SPRING

```java
@Configuration

@Bean

@Autowired VS @Resource
```



### Optional

- JPA findById의 반환 값
- `.isParent() .get() .filter()` 등의 메소드를 사용할 수 있음



### DTO

- Data Transfer Object
- VO = DTO의 ReadOnly



### Model Mapper

- dto 와 model 을 이어주는 라이브러리



### @Configuration / @Bean

- 외부 library를 bean으로 등록할 때 써야함



### @Component

- 내가 만든 class를 Bean처럼 등록할 때 써야함

  

### 고차함수

- 함수의 매개변수로 함수를 받을 수 있어야함
- lambda