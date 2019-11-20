# Oracle TimeStamp를 Java에서 못가져 올 때

- Json으로 변경되기 어려운 경우에 발생하는데 Oracle의 timestamp형식이 변환되지 않음



## 해결방법

`Select Cast(SYSTIMESTAMP AS DATE) DT From dual;`

Oracle 형변환

```java
Date date = oracleTimestamp.dateValue(); 
System.out.println(date);

```

java 형변환