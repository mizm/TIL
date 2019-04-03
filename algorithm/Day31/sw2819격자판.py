dx = [0,1,0,-1]
dy = [-1,0,1,0]
def issafe(x,y) :
    return x >= 0 and x < 4 and y >= 0 and y < 4
def dfs(pos,x,y,item) :
    if pos == 6 :
        # print(item)
        if not item in res :
            res.append(item)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if issafe(nx,ny) :
            dfs(pos+1,nx,ny,item*10+m[ny][nx])
for tc in range(int(input())) :
    m = []
    res = []
    for i in range(4) :
        m.append(list(map(int,input().split())))
    for i in range(4) :
        for j in range(4) :
            dfs(0,i,j,m[j][i])
    print("#%d %d"%(tc+1,len(res)))