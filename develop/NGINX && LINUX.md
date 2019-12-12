# NGINX && LINUX

### LINUX - REDHAT 계열



1. 저장소 설치

```bash
wget http://nginx.org/packages/rhel/6/noarch/RPMS/nginx-release-rhel-6-0.el6.ngx.noarch.rpm
rpm -ivh nginx-release-rhel-6-0.el6.ngx.noarch.rpm
sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

2. nginx 설치

```bash
yum -y install nginx
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



403 forbidden 에러 시

blog.naver.com/PostView.nhn?blogId=cloverloop&logNo=140208992571&proxyReferer=https%3A%2F%2Fwww.google.com%2F



모든 경로의 권한을 최소 755로 바꿔줘야함

경로가 /home/webprod/test/dist 이면

home 부터 하나하나 권한 확인필요