def check() :
    startx , starty = SearchXY(True)
    endx, endy = SearchXY(False)
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    queue = [(0,0)] * (n**3)
    front = rear = -1
    rear += 1
    queue[0] = (startx,starty)
    while front != rear :
        front += 1
        x,y = queue[front]
        for i in range(4) :
            newx = x+dx[i]
            newy = y+dy[i]
            if newx == endx and newy == endy :
                return 1
            if issafe(newx,newy) :
                rear += 1
                queue[rear] = (newx,newy)
                mymap[newy][newx] = 1
    return 0

def issafe(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n and mymap[y][x] == 0

def SearchXY(flag) :
    for i in range(n) :
        for j in range(n) :
            if mymap[i][j] == 2 and flag:
                return j,i
            if mymap[i][j] == 3 and not flag:
                return j,i
for tc in range(int(input())) :
    n = int(input())
    mymap = []
    for i in range(n) :
        mymap.append([int(x) for x in input()])
    print(f'#{tc+1} {check()}')