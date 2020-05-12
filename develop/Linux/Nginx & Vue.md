# Nginx & Vue

vue의 웹서버로 nginx를 사용하면 router url 때문에 새로고침할 시 404error를 발생함



router의 모드를 hash모드로 변경



history mode



```
server {
    listen 80;
    listen [::]:80;

    root  /home/webprod/CPFR/dist;

    index index.html;

    server_name  mesif.ildong.com;

    location / {
        try_files $uri $uri/ @rewrites;
    }

    location @rewrites {
        rewrite ^(.+)$ /index.html last;
    }

    location ~* \.(?:ico|css|js|gif|jpe?g|png)$ {
        expires max;
        add_header Pragma public;
        add_header Cache-Control "public, must-revalidate, proxy-revalidate";
    }

    error_page   500 502 503 504  /50x.html;

    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

