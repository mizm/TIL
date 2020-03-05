# ORACLE auto_increment

**CREATE SEQUENCE 시퀀스이름 START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 99999999;**

****

**설명**

**START WITH : 시작 값 지정**

**INCREMENT BY : 증가할 값 지정**

**MAXVALUE : 최대 값 지정**

**MINVALUE : 최소 값 지정**

****

**위와 같이 시퀀스를 생성 한 뒤에, Insert시나 각 사용할 명령어에 시퀀스를 활용하여 사용한다.**



**예시)**

**예시에서는 컬럼1은 자동증가 컬럼, 컬럼2는 varchar로 설정한다고 가정한다.**

**INSERT INTO 테이블명(컬럼1,컬럼2) VALUES(시퀀스이름.NEXTVAL,'test');**

**NEXTVAL은 자동증가할 숫자를 가져온다.**



**SELECT 시퀀스이름.NEXTVAL FROM DUAL;**

**위의 명령어를 통하여, 다음 자동증가 값을 가져올 수 있다.**

