import sys
sys.stdin = open('bj14889.txt','r')

N = int(input())
power = []
for i in range(N) :
    power.append(list(map(int,input().split())))

team = [0 for i in range(N)]
res = 100 * 20 * 20
def dfs(n) :
    global res
    if n >= N :
        if sum(team) == N/2:
            blue = []
            red = []
            for i in range(N) :
                if team[i] == 0 :
                    blue.append(i)
                else :
                    red.append(i)
            bluePoint = 0
            redPoint = 0
            for i in range(N//2) :
                for j in range(i+1,N//2) :
                    bluePoint += power[blue[i]][blue[j]]
                    bluePoint += power[blue[j]][blue[i]]
                    redPoint += power[red[i]][red[j]]
                    redPoint += power[red[j]][red[i]]
            if abs(bluePoint - redPoint) < res :
                res = abs(bluePoint - redPoint)
        return
    team[n] = 1
    dfs(n+1)
    team[n] = 0
    dfs(n+1)

dfs(0)
print(res)