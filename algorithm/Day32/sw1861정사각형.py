dx = [0,1,0,-1]
dy = [-1,0,1,0]
def issafe(x,y,item) :
    return x >= 0 and x < n and y >= 0 and y < n and m[y][x] - 1 == item
def dfs(x,y,cnt,ox,oy) :
    global res,idx
    k = m[y][x]
    if cnt > res:
        res = cnt
        idx = m[oy][ox]
    if cnt == res :
        if idx > m[oy][ox] :
            idx = m[oy][ox]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if issafe(nx,ny,k) :
            dfs(nx,ny,cnt+1,ox,oy)
for tc in range(int(input())) :
    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(int,input().split())))
    c = [[-1]*n for i in range(n)]
    res = 0
    idx = n**2+1
    for i in range(n) :
        for j in range(n) :
            dfs(i,j,1,i,j)
    print("#%d %d %d" % (tc + 1, idx, res))