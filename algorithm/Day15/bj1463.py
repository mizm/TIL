def dp(n) :
    for i in range(1,n+1) :
        if c[i] == -1 :
            c[i] = 0
        if i * 3 <= n :
            if c[i*3] == -1 :
                c[i*3] = c[i] + 1
            else :
                c[i*3] = min(c[i*3],(c[i]+1))
        if i*2 <= n:
            if c[i*2] == -1 :
                c[i*2] = c[i] + 1
            else :
                c[i*2] = min(c[i*2],c[i]+1)
        if i+1 <= n :
            if c[i+1] == -1 :
                c[i+1] = c[i] + 1
            else :
                c[i+1] = min(c[i+1],c[i]+1)

n = int(input())
cnt = 0
c = [-1]*(n+10)


dp(n)
print(c[n])