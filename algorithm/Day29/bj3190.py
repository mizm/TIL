n = int(input())
k = int(input())
m = [[0]*n for i in range(n)]
change = {}

for i in range(k) :
    a,b = map(int,input().split())
    m[a-1][b-1] = 1
l = int(input())
for i in range(l) :
    a, b = input().split()
    change[int(a)] = b

def issafe(x,y) :
    return x >= 0 and x < n and y>=0 and y < n and m[y][x] >= 0
t = 0
x=y=0
tax=tay=0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dir = 0
m[0][0] = -1
snake = [(0,0)]
while 1 :
    t += 1
    chk = change.get(t)

    tx = x+dx[dir]
    ty = y+dy[dir]
    if not issafe(tx,ty) :
        break
    if m[ty][tx] == 0 :
        m[ty][tx] = -1
        snake.insert(0,(tx,ty))
        tax,tay = snake.pop()
        m[tay][tax] = 0
    elif m[ty][tx] == 1:
        snake.insert(0, (tx, ty))
        m[ty][tx] = -1

    x = tx
    y = ty
    if chk:
        if chk == 'D':
            dir += 1
            dir %= 4
        if chk == 'L':
            dir -= 1
            if dir == -1:
                dir = 3
print(t)