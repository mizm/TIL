def chk(n):
    t = 9
    while n >= 1:    
        if t >= n%10 :
            t=n%10
            n=n//10
        else:
            return False
    return True
for i in range(int(input())) :
    q = 0
    n = int(input())
    l = list(map(int,input().split()))
    for k in range(n-1) :
         for t in range(n-1-k):
            p = l[k]*l[t+k+1]
            if chk(p) and p > q :
                q = p
    print(f'#{i+1} {q}')