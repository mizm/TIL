def dfs(pos,money,time) :
    if time > k :
        return -99
    if dp[pos][time] == -99 :
        return -99

    if pos == n-1 and time <= k :
        return money
    if dp[pos][time] != -1 :
        return dp[pos][time] + money
    t = -99
    t = max(t,dfs(pos+1,money+item[pos+1][1],time+item[pos+1][0]))
    t = max(t,dfs(pos+1,money+item[pos+1][3],time+item[pos+1][2]))
    if t == -99 :
        dp[pos][time] = -99
    else :
        dp[pos][time] = t-money

    return t

n,k = map(int,input().split())
item = []
dp = [[-1]*(100001) for i in range(n)]

for i in range(n) :
    item.append(list(map(int,input().split())))
# print(dp)

re = dfs(0,item[0][1],item[0][0])
re = max(re,dfs(0,item[0][3],item[0][2]))
print(re)