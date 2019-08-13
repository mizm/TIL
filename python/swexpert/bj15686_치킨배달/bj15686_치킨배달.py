import sys
sys.stdin = open('bj15686.txt','r')
def dfs(pos,item) :
    global M,count,distance,res
    if len(item) == M:
        re = 0
        for d in distance :
            t = 500
            for i in item :
                if d[i] < t :
                    t = d[i]
            re += t
            if re > res :
                return
        if re < res :
            res = re
        return
    for i in range(pos,count) :
        if i in item and i < pos:
            continue
        item.append(i)
        dfs(i+1,item)
        item.pop(len(item)-1)
N,M = list(map(int,input().split()))
map=[list(map(int,input().split())) for i in range(N)]
distance = []
home = []
cc = []
for i in range(N) :
    for j in range(N) :
        if map[i][j] == 1 :
            home.append([i+1,j+1])
        elif map[i][j] == 2 :
            cc.append([i+1,j+1])
count = len(cc)
for h in home :
    temp = []
    for c in cc :
        temp.append(abs(h[0]-c[0])+abs(h[1]-c[1]))
    distance.append(temp)
item = []
res = 987654321
dfs(0,item)
print(res)

