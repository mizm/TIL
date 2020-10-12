# SpringBoot JsonParser

```json
{
    items : [
        {
            id : 1 
        },
        {
            id : 2
        }
    ]
}
```

위와 비슷한 형식의 JSON FILE일 경우에 Java에서 Parsing할 때

```java
JsonParser parser = new BasicJsonParser();

Map<String, Object> jsonMap = parser.parseMap(response.body().string());

ArrayList<Map<String,Object>> t = (ArrayList) jsonMap.get("items");
//ArrayList로 형변환 해줘야함 Object로 받아와져서 그런가봄
System.out.println(t);
for(int i = 0; i < t.size(); i++) {
    System.out.println(t.get(i));
}


```



