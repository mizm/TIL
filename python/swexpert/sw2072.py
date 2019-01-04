for i in range(int(input())) :
   print(f'#{i+1} {sum(map(lambda x: x if x%2 else 0  ,map(int,input().split())))}')
