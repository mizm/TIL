# Git Lab SSH key 만들기

1. ssh key 가 있는지 확인

   ```bash
   cat ~/.ssh/id_rsa.pub
   ```

   

2. 없는 경우 후 엔터엔터엔터엔터

   ```bash
   ssh-keygen -t rsa -C "GitLab" -b 4096
   ```

   

3. 다시 확인하면

   ```bash
   cat ~/.ssh/id_rsa.pub
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDONBI8Qm0Q0DZdpTXpY7nte7fagerF1S1P.....
   위 의 값을 git lab ssh key에 넣어두면됨
   ```

   