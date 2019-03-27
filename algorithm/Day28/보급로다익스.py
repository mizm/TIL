def issafe(x,y) :
	return x >= 0 and x < n and y >= 0 and y < n and v[y][x] == 0

for tc in range(int(input())):
    n = int(input())
    m = []
    min_v = 987654321
    v = [[0]*n for i in range(n)]
    c = [[min_v] * n for i in range(n)]
    for i in range(n) :
        m.append(list(map(int,list(input()))))

    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    c[0][0] = 0
    c[1][0] = m[1][0]
    c[0][1] = m[0][1]
    x=y=0
    tt = 0
    while x!= n-1 and y != n-1 :
        mx=my=temp=min_v
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if issafe(nx,ny):
                if temp > m[ny][nx]+c[y][x] :
                    temp = m[ny][nx]+c[y][x]
                    c[ny][nx] = temp
                    mx = nx
                    my = ny
        tt += temp
        x = mx
        y = my
    print(temp)


    print("#%d %d"%(tc+1,c[n-1][n-1]))