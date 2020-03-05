# Jmeter 성능 분석기

1. 설치

   - http://jmeter.apache.org/download_jmeter.cgi

2. 실행

   - `bin / jmeter.bat` 실행 (.bat 창을 끄면 종료됨)

3. 시작하기 `test plan -> add -> threads(users) -> threads group`

   ![1576213322174](C:\Users\ydh\AppData\Roaming\Typora\typora-user-images\1576213322174.png)

4. Thread Group Setting

   **Action to be taken after a Sampler error** 이부분은 실행 중에 에러가 발생하면 처리할 방법을 선택

   Number of Threads ( users ) : 쓰레드의 갯수를 선택합니다. 유저의 수

   Ramp-Up Period ( in seconds ) : 쓰레드가 여러개면 여러개의 실행시간을 users로 계산해서 실행

   Loop Count : user가 테스트할 반복할 횟수를 넣어주시면 됩니다.

   ![1576213475814](C:\Users\ydh\AppData\Roaming\Typora\typora-user-images\1576213475814.png)

5. `Thread Group 우클릭 -> Add > Config Element > HTTP Cookis Manager`

6. `Thread Group 우클릭 -> Add > Logic Controller > Once Only Controller`

7. `Once Only Controller 우클랙 -> Add > Sample > HTTP Request`

8. HTTP Request setting

   - **Name** : doLogin ( 나중에 Request 가 많아져 헷갈릴수 있으니 Name을 설정해줍니다. )

   - **Server Name or IP** : localhost ( http:// 를 제외한 주소를 적어줍니다. )

   - **Port Number** : 80 ( 사용하시는 포트를 입력해주시면 되구요, )

   - **Method** : POST ( 저는 POST방식으로 로그인을 해서 POST를 설정했는데 GET방식이시면 GET으로 하시면 됩니다. ) 

   - **Path** : /common/doLogin.do ( 주소뒤에 해당 mapping 주소를 입력해줍니다. )

   - **Parameters** : ( 실제 로그인 하실 계정정보를 입력해주시면됩니다. )

      \- **id** : admin (  저는 id라고 적었는데 해당 input의 id값을 적어주시면 됩니다. ex) id="user_id" 이시면 user_id )

      \- **pw** : admin ( input의 pw의 id값을 적어주시구요.)