# Oracle TimeStamp 사용



`select * from cms_contents AS OF TIMESTAMP(SYSTIMESTAMP-INTERVAL '30' MINUTE);`

30 분 전의 cms_contents를 보여준다.

