# Jenkins 원격지 linux 서버 셋팅

### 

```bash
//혹시 모르니 권한 777
mkdir -m 777 path

//열려있는 모든 포트 확인
netstat -nap
//확인하려는 포트 상태 확인
netstat -nap |grep '포트번호'
//현재 listen중인 포트 확인
netstat -nap |grep LISTEN
//포트열기
iptables -I INPUT 1 -p tcp --dport 11045 -j ACCEPT
//포트 삭제
iptables -D INPUT -p tcp --dport 11045 -j ACCEP
iptables -D INPUT 1
```



## 1. Credential 세팅

- 젠킨스 Credentials - System - Global credentials 을 클릭하면 좌측에 add credentials가 있음

![1574644438121](C:\Users\ydh\AppData\Roaming\Typora\typora-user-images\1574644438121.png)

- Username에 아이디 password에 비밀번호 입력 (Git LAB)
- Item에 소스 코드 관리 repository 주소 입력
- credentials 아까 만든걸로 수정



## 2. Build Gradle Script

- Item - 구성 - Build 탭 - Add build Step - Invoke Gradle Script - Use Gradle Wrapper

![1574645335324](C:\Users\ydh\AppData\Roaming\Typora\typora-user-images\1574645335324.png)



## 3. 빌드 후 조치 - Gradle

- 빌드 후 조치 추가 - Send build artifacts over SSH'
- Source files -  build/libs/생성된 jar 파일명
- Remove prefix - build/libs  (jar파일만 가져오기 위해서)
- Remote directory - BackEnd/SendApi (원격지 주소)
- Exec Command = cd Backend/SendApi; ./start.sh restart (보낸 후에 실행될 스크립트)



## 4. SSH Server 추가 

- jenkins 환경설정 - SSH servers 에 추가

