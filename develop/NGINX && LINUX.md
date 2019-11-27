# NGINX && LINUX

### LINUX - REDHAT 계열



1. 저장소 설치

```bash
wget http://nginx.org/packages/rhel/6/noarch/RPMS/nginx-release-rhel-6-0.el6.ngx.noarch.rpm
rpm -ivh nginx-release-rhel-6-0.el6.ngx.noarch.rpm
```

2. nginx 설치

```bash
yum install nginx
```

3. nginx 설정

```bash
sudo find / -name nginx.conf
# nginx.conf 파일 찾기
vi nginx.conf
location {
	root  <이부분을 원하는 경로로 변경>
}
i를 누르면 insert모드로 진입함 현재 커서의 위치
:wq 입력
저장 후 나가기
```

