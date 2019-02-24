def check() :
    startx , starty = SearchXY(True)
    endx, endy = SearchXY(False)
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    stack = [(0,0)]*(n*n*n)
    top = 0
    stack[top] = (startx,starty)
    while top >= 0 :
        x,y = stack[top]
        mymap[y][x] = 1
        top -= 1
        for i in range(4) :
            newx = x+dx[i]
            newy = y+dy[i]
            if newy == endy and newx == endx :
                return 1
            if issafe(newx,newy,stack) : 
                top += 1
                stack[top] = (newx,newy)   
    return 0
def issafe(x,y,stack) :
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
    print(mymap)
    print(check())