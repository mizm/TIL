def dfs(pos,time,money) :
    if time > k :
        return -1
    if pos > n :
        return -1
    dp[pos][time] = money
    if pos+1 <= n and dp[pos+1][time+item[pos][0]] < money+item[pos][1] and dp[pos+1][time+item[pos][0]] != -1 :
        if dfs(pos+1,time+item[pos][0],money+item[pos][1]) == -1 :
            dp[pos+1][time] = max(dp[pos])
    if pos+1 <= n and dp[pos+1][time+item[pos][2]] < money+item[pos][3] and dp[pos+1][time+item[pos][2]] != -1:
        if dfs(pos + 1, time + item[pos][2], money + item[pos][3]) == -1 :
            dp[pos + 1][time] = max(dp[pos])



n,k = map(int,input().split())
item = []
dp = [[0]*(100001) for i in range(n+2)]

for i in range(n) :
    item.append(list(map(int,input().split())))
# print(dp)
dfs(0,0,0)

print(max(dp[n]))