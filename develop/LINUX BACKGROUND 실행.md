# LINUX BACKGROUND 실행

1. 사용자가 로그아웃해도 백그라운드로 실행되게 하는 명령어

   `$ nohup java -jar abcdefg.jar &`

 

2. 프로세스 종료
   - 찾기 : `ps –ef | grep 'abcdefg'`
   - 종료 : `kill -9 (pid)`

