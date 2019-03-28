def issafe(x,y) :
    return x >= 0 and x < m and y >= 0 and y < n and my_map[y][x] != '#'
def dfs(pos,x1,y1,x2,y2) :
    global max_v
    if pos > max_v:
        return
    #위
    for i in range(4):
        tx1 = x1
        tx2 = x2
        ty1 = y1
        ty2 = y2

        #아래

        #오른쪽

        #왼쪽

n,m = map(int,input().split())
my_map = []
max_v = 10
rx=ry=0
bx=by=0
x=y=0
dx = [0,1,0,-1]
dy = [-1,0,1,0]
for i in range(n) :
    my_map.append(list(input()))
    for j in range(m) :
        if my_map[i][j] == "R" :
            rx = j
            ry = i
        elif my_map[i][j] == "B" :
            bx = j
            by = i
        elif my_map[i][j] == "O":
            x = j
            y = i
print(rx,ry,bx,by)
dfs(0,rx,ry,bx,by)
print(max_v)