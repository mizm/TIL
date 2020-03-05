# NGINX SSL 적용 후 TTFB TIMEOUT 1분으로 떨어짐



## proxy 쪽이나 어디 연결 될때 1분이 기본 설정으로 되어있어서 1분이 넘으면 error를 뱉음



```
 server {
    listen              443 ssl;
    server_name         localhost;
    client_max_body_size 200M;
    
    #ssl             on;
    ssl_certificate             /etc/nginx/ssl/nginx_ssl.crt;
    ssl_certificate_key         /etc/nginx/ssl/_wildcard_ildong_com_SHA256WITHRSA.key;

    ssl_session_cache       shared:SSL:10m;
    ssl_session_timeout     10m;

    ssl_protocols       SSLv2 SSLv3 TLSv1.2;
    ssl_ciphers         HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers   on;

    proxy_connect_timeout       605;
    proxy_send_timeout          605;
    proxy_read_timeout          605;
    send_timeout                605;
    keepalive_timeout           605;
    client_body_timeout 10m;
}
```

timeout 관련 된 정보와

ssl_session_cache에 마지막에 10m으로 늘려줌

