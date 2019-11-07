# Vue - computed & watch

## computed

- computed에 return에 걸려있는 특정 값에 의존해서 그 값이 변할 때 computed 내부 함수가 실행

  ```vue
  computed : {
  	check : function() {
  		return this.message
  	}
  }
  // 이 상황에서는 this.message가 변경되면 computed가 실행됨
  
  ```

- 선언적으로 의존관계를 만듬.

- **computed 속성은 종속 대상을 따라 저장(캐싱)된다는 것** 입니다. computed 속성은 해당 속성이 종속된 대상이 변경될 때만 함수를 실행합니다.

- 즉 `message`가 변경되지 않는 한, computed 속성인 `reversedMessage`를 여러 번 요청해도 계산을 다시 하지 않고 계산되어 있던 결과를 즉시 반환합니다.



## watch

- `watch` 옵션을 통해 데이터 변경에 반응하는 보다 일반적인 방법을 제공합니다. 이는 데이터 변경에 대한 응답으로 비동기식 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 가장 유용합니다.
- 

