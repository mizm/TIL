환경 마다 oracle 으로 요청 시에 언어 환경이 달라지는 경우가 있음.

기본 로컬의 환경을 가져가서 쿼리를 실행하기 때문에 변경이 필요함.



# 로컬 환경 확인 및 변경

## 로컬 LANG 환경 확인

```bash
echo $LANG
-- 현재 설정된 로케일 확인 명령
locale -a
-- 모든 로케일 확인
```



## 로컬 LANG 환경 변경

```bash
vi /etc/sysconfig/i18n
```

- vi 환경에서 i를 입력하면 insert 모드
- Backspace  작동 안함 delete키로 지우고 새로 작성
- esc 버튼 후 :wq 저장후 종료