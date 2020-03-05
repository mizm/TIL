# PowerShell

1. log tail 명령어

Get-Content .\production.log -Wait -Tail 100

2. 한글 깨짐

   ## `Powershell` 에서 `git log` 명령 실행시 한글로 작성된 커밋 메시지가 깨져 보이는 현상

   ```
   `commit bd269780b5c888b0ea86939f3dd08c12e68ef595``Author: coozplz <coozplz@gmail.com>``Date:   Mon Aug 22 19:44:26 2016 +0900` `    ``?뚯씠釉??뺣낫 異붽?` `commit 23f13d59f8bc9f7e53fc91f322b8dfbbfddf0f95``Author: coozplz <coozplz@gmail.com>``Date:   Mon Aug 22 16:51:15 2016 +0900` `    ``臾몄꽌 ?낅뜲?댄듃`
   ```

   위와 같은 문제 해결을 위해 `git` 명령 실행 결과를 디코딩과 인코딩 하는 작업을 하면서 확인 했었는데 보다 간단한 해결 방법을 찾았습니다.

   ### **1. Powershell 프로필 위치 확인**

   ```
   `PS C:> ``$profile``C:\Users\coozplz\Documents\WindowsPowerShell\Microsoft.PowerShellISE_profile.ps1`
   ```

   ### **2. $profile 값에 인코딩 변경 추가**

   ```
   `# filename: Microsoft.PowerShellISE_profile.ps1` `$env:LC_ALL='C.UTF-8'`
   ```

   ### **3. Powershell 창에서 확인**

   ```
   `commit bd269780b5c888b0ea86939f3dd08c12e68ef595``Author: coozplz <coozplz@gmail.com>``Date:   Mon Aug 22 19:44:26 2016 +0900` `    ``테이블 정보 추가` `commit 23f13d59f8bc9f7e53fc91f322b8dfbbfddf0f95``Author: coozplz <coozplz@gmail.com>``Date:   Mon Aug 22 16:51:15 2016 +0900` `    ``문서 업데이트`
   ```

   정상적으로 표시되는 것을 확인할 수 있습니다.

   ### Share this: