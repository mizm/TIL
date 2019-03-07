def issafe(x,y,z) :
    return x >= 0 and x < n and y >= 0 and y < n and p[y][x] != z and p[y][x] > 0
def ispossible(tx,ty,dx,dy,z) :
    tx += dx
    ty += dy
    k = 1 if z==2 else 2
    while issafe(tx,ty,z) :
        tx += dx
        ty += dy
    return issafe(tx,ty,k)

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]
for tc in range(int(input())) :
    n,m = map(int,input().split())
    p = [[0]*n for i in range(n)]
    p[n//2-1][n//2-1] = 2
    p[n//2-1][n//2] = 1
    p[n//2][n//2-1] = 1
    p[n//2][n//2] = 2
    for i in range(m) :
        y,x,z=map(int,input().split())
        y-=1
        x-=1
        p[y][x] = z
        for j in range(8) :
            tx = x
            ty = y
            if ispossible(tx,ty,dx[j],dy[j],z) :
                while issafe(tx+dx[j],ty+dy[j],z) :
                    tx += dx[j]
                    ty += dy[j]
                    p[ty][tx] = 2 if z == 2 else 1
    b = w = 0
    for i in p :
        b+= i.count(1)
        w+= i.count(2)
    print('#%d'%(tc+1),b,w)