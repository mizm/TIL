# 계층형쿼리 CONNECT_BY_ROOT
CONNECT_BY_ROOT는 계층형 쿼리에서 최상위 로우를 반환하는 연산자다. 연산자이므로 CONNECT_BY_ROOT 다음에는 표현식이 온다.

입력

```sql
 SELECT department_id,
       LPAD(' ' , 3 * (LEVEL-1)) || department_name,
       LEVEL,
       CONNECT_BY_ROOT department_name AS root_name
  FROM departments START WITH parent_id IS NULL CONNECT BY PRIOR department_id = parent_id;
```



