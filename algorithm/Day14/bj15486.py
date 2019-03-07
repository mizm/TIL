def dp(a, time, money):
    if a+time <= n:
        for i in range(a,a+time) :
            c[a][i] = money


n = int(input())
p = [0]*n
t = [0]*n
for i in range(n) :
    t1,p1 = map(int,input().split())
    t[i]=t1
    p[i]=p1

c = [[-1]*(n+1) for i in range(n+1)]

for i in range(n) :
    dp(i,t[i],p[i])

for i in c :
    print(i)
