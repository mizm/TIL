# spring boot 동작 방식

1. Controller로 등록된 class file로 http 요청이 옴
2. Controller에 맵핑되어 있는 함수 실행
3. 만약 Service Class를 실행하면 해당 Service Class 로 이동
4. Service Class에서 mapper가 맵핑 되어있으면 mapper.java로 이동
5. mapper.java는 mapper.xml과 (@Repository)를 통해 맵핑
6. ** 만약 interceptor을 @Configuration을 통해 선언하면 1번 이전에 interceptor에 들림 (Filter 도 비슷한 기능 확인필요)

