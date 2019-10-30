# Spring Boot application 에서 경로



## h2 에서 사용하다가 생긴 issue

```java
#~./
spring.db2.datasource.jdbc-url=jdbc:h2:../backend/~/testdb;
```

jar파일로 실행시 기존 경로가 작동을 안하길래  ..경로로 상위 폴더로 이동 후에 다시 접근하니 작동

처음부터 잘못한건지 다시 한번 확인해봐야함.