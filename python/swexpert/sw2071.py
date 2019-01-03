n = int(input())
for i in range(n) : 
    t = list(map(int,input().split()))
    print(f'#{i+1} {int(round(sum(t)/len(t)))}')
