# Rest의 구성

- 지원(Resource) - URI
- 행위(Verb) - HTTP method
- 표현(Representations)

# REST API 디자인 가이드

1.  URI는 정보의 자원을 표현해야 한다.
2. 자운에 대한 행위는 HTTP Method(GET,POST,PUT,DELETE)로 표현한다.

# 예시

```html
GET /movies/shows/1	 (x)
GET /movies/1		(o)
```

```
GET	/movies/create (x) - GET Method는 자원 생성에 부적합
POST /movies	   (o)
```

```
GET /movies/2/update (x) - GET 부적합
PUT /movies/2
```

```
GET /movies/2/edit    (X)
PUT /movies/2  		  (O)
```



