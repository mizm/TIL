# DDD - Basic

### Entity

- 존재간에 구별할 수 있는 모델 (식별자 : ID가 있음)
- EX) JPA의 Table

### Value Object

- 식별자가 필요 없는 고유 모델
- 불변하는 상태나 값

### Aggregate

- 생명주기가 동일한 모델을 모아 놓은 Root 모델

### Service

- 도메인 간의 연산을 처리하는 모델

### Repository

- 모델을 저장하는 곳

### Factory

- entity, aggregate를 생성하는 모델

## Layered Architecture

### Interface 

- 사용자의 요청을 하위 레이어로 전달하는 역할

### Application

- 복잡한 비즈니스 로직을 처리하는 레이어

### Domain

- 도메인에 대한 정보, 객체의 상태, 도메인의 비즈니스 로직 제공

### Infrastructure

- 영속성 구현, 외부와의 통신기능 제공