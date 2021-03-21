# Async 방법
1. @EnableAsync 설정
2. 아래와 같은 클래스를 만든다.
```java
@Configuration
@EnableAsync
public class AsyncThreadConfiguration {
	@Bean
	public Executor asyncThreadTaskExecutor() {
		ThreadPoolTaskExecutor threadPoolTaskExecutor = new ThreadPoolTaskExecutor();
		threadPoolTaskExecutor.setCorePoolSize(8);
		threadPoolTaskExecutor.setMaxPoolSize(8);
		threadPoolTaskExecutor.setThreadNamePrefix("line-call-pool");
		return threadPoolTaskExecutor;
	}

}
```

3. `public` 메서드에만 동작한 Spring AOP를 통한 프록시객체로 생성되기 때문에.
    - CompletableFuture를 통해 return값을 준다.
```java
// Class MessageSender
    @Async
	public CompletableFuture<LineMessage.LineResponse> sendAsync(String id) {
		OkHttpClient client = new OkHttpClient();
		Response response = null;
		List<String> res = new ArrayList<>();
		String text = null;
		try {
			response = client.newCall(sendStrategy.setRequest()).execute();
			text = response.body().string();
		} catch(IOException e) {
			//IOException을 RuntimeException으로 포장해서 던지고 종료한다.
			text = e.getMessage();
		} finally {
			//성공 실패 리턴
			response.close();
			return new AsyncResult<>(new LineMessage.LineResponse(id,text)).completable();
		}
	}

```


4. 받는 곳
```java
// Class AsyncSenderProxy
public List<LineMessage.LineResponse> sendAsync(LineMessage.LineRequest msg)  {

		List<LineMessage.LineResponse> responses = new ArrayList<LineMessage.LineResponse>();
        // Async 호출 후 Future을 받아오기 위한 리스트
		List<CompletableFuture<LineMessage.LineResponse>> futureList = new ArrayList<>();
		try {
			for (LineMessage.Account account : msg.getAccountIds()) {
				messageSender.setSendStrategy(sendMessageStrategy(msg, account.getId()));
				futureList.add(messageSender.sendAsync(account.getId()));
			}
            // allOf를 통해 모든 Future의 호출이 종료될 때까지 대기한뒤
			CompletableFuture.allOf(futureList.toArray(new CompletableFuture[msg.getAccountIds().size()]));
            // 받아온 값을 .get()을 통해 설정한다.
			for (CompletableFuture<LineMessage.LineResponse> future : futureList) {
				responses.add(future.get());
			}
		} catch (ExecutionException e) {
			throw new RuntimeException(e.getMessage());
		} catch (InterruptedException e) {
			throw  new RuntimeException(e.getMessage());
		}
		return responses;
}
```