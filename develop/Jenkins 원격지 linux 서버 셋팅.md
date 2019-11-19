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
netstat -nal |grep LISTEN
//포트열기
iptables -I INPUT 1 -p tcp --dport 11045 -j ACCEPT
//포트 삭제
iptables -D INPUT -p tcp --dport 11045 -j ACCEP
iptables -D INPUT 1
```

