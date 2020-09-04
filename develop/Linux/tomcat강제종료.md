일반적으로 톰캣을 구동하고 종료하는 명령어는 $TOMCAT_HOME/bin/ 에 있는 startup.sh 와 shutdown.sh 이다.
그런데 리눅스 서버에서 톰캣을 운영하다 보면 종종 어이없는 일이 발생을 한다.

그중에 하나가 shutdown.sh 명령을 실행했음에도 불구하고 톰캣이 죽지 않는 상황이 발생할 때가 있다.

물론 이 경우 리눅스에서 PID를 확인 한 후에 kill -9 명령어를 통해 톰캣 프로세스를 종료시킬 수는 있으나
매번 이렇게 종료시키에는 귀찮음이 따른다.

이럴때는 CATALINA_PID를 이용하여 shutdown.sh에 force 옵션을 사용하면 된다.

CATALINA_PID를 지정하게 되면 톰캣이 구동될때 프로세스ID를 해당 파일에 기록하게 되며, shutdown시
해당 PID를 종료시킴으로서 kill -9 명령어와 동일한 결과를 낼수 있다.

일단 톰캣 기본 설정에는 CATALINA_PID가 지정되어 있지 않다. catalina.sh 파일을 열어 아래와 같이 추가한다.


**catalina.sh**



```bash
 # resolve links - $0 may be a softlink  
 PRG="$0"   
 while [ -h "$PRG" ]; do    
 	ls=`ls -ld "$PRG"`    
 	link=`expr "$ls" : '.*-> \(.*\)$'`    
 	if expr "$link" : '/.*' > /dev/null; then      
 		PRG="$link"    
 	else      
 		PRG=`dirname "$PRG"`/"$link"    
 	fi  
 done   CATALINA_PID=/usr/local/tomcat7/bin/tomcat.pid
# Get standard environment variables 
PRGDIR=`dirname "$PRG"`
```







그 다음 shutdown.sh 파일을 열어 stop 명령어 뒤에 -force 옵션을 추가하면 된다.



**shutdown.sh**

```shell
# Check that target executable exists
 if $os400; then
   # -x will Only work on the os400 if the files are:
   # 1. owned by the user
   # 2. owned by the PRIMARY group of the user
   # this will not work if the user belongs in secondary groups
   eval
 else
   if [ ! -x "$PRGDIR"/"$EXECUTABLE" ]; then
     echo "Cannot find $PRGDIR/$EXECUTABLE"
     echo "The file is absent or does not have execute permission"
     echo "This file is needed to run this program"
     exit 1
   fi
 fi

 exec "$PRGDIR"/"$EXECUTABLE" stop -force "$@"



```









위 내용은 톰캣6, 7에서 모두 동일하게 사용이 가능하다.

