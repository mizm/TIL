
def dfs(pos,money) :
    if pos >= n :
        return money
    if pos + t[pos] > n:
        return money

    if c[pos] != -1 :
        return c[pos] + money
    k1=-2
    k1 = max(k1,dfs(pos + t[pos], money + p[pos]))
    k1 = max(k1,dfs(pos+1,money))
    if k1 == -2 :
        c[pos] = -2
    else :
        c[pos] = k1 - money
    return k1



n = int(input())
p = [0]*n
t = [0]*n
for i in range(n) :
    t1,p1 = map(int,input().split())
    t[i]=t1
    p[i]=p1
c = [-1]*(n+1)
print(dfs(0,0))
# print(c)