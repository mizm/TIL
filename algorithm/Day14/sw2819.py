def bfs(x,y) :
    q = [(x,y)]
    while q :
        x1,y1 = q.pop()
        newx = x1
        newy = y1
        for i in range(4):
            newx += x1+dx[i]
            newy += y1+dy[i]
            if issafe(newx,newy) :
                q.append((newx,newy))
def issafe(x,y) :
    return 0<=x<4 and 0<=y<4
dx = [0,0,1,-1]
dy = [1,-1,0,0]
data = []
item = []
for tc in range(int(input())) :
    data.append(list(map(int,input().split())))
for i in range(4) :
    for j in range(4) :
