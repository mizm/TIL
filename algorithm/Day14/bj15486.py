# def dfs(pos,money) :
#     if pos >= n :
#         return money
#     if pos + t[pos] > n:
#         return money
#
#     if c[pos] != -1 :
#         return c[pos] + money
#     k1=c[pos]
#     k1 = max(k1,dfs(pos + t[pos], money + p[pos]))
#     k1 = max(k1,dfs(pos+1,money))
#     c[pos] = k1 - money
#     return k1
def dp() :
    for i in range(n) :
        if c[i] == -1 :
            c[i] = 0
        if i + t[i] <= n :
            if c[i+t[i]] == -1 :
                c[i + t[i]] = c[i] + p[i]
            else :
                c[i+t[i]] = max(c[i+t[i]],(c[i]+p[i]))
        if i+ 1 <= n:
            if c[i+1] == -1 :
                c[i+1] = c[i]
            else :
                c[i+1] = max(c[i+1],c[i])


n = int(input())
p = [0]*n
t = [0]*n
for i in range(n) :
    t1,p1 = map(int,input().split())
    t[i]=t1
    p[i]=p1
c = [-1]*(n+1)

dp()
print(c[n])