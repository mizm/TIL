

# LINUX PORT 열기, 조회, 삭제

1. 포트확인

   `netstat -nap`

   `netstat -nap |grep '포트번호'`

   `nestat -nap |grep LISTEN` 현재 LISTEN중인 포트

2. 포트열기

     `iptables -I INPUT 1 -p tcp --dport 포트번호 -j ACCEPT`

3. 포트 삭제

   `  iptables -D INPUT -p tcp --dport 11045 -j ACCEPT`

