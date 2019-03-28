def issafe(x,y) :
	return x >= 0 and x < n and y >= 0 and y < n

for tc in range(int(input())):
    n = int(input())
    m = []
    min_v = 987654321
    c = [[min_v] * n for i in range(n)]
    for i in range(n) :
        m.append(list(map(int,input().split())))

    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    Q = [(0,0)]
    c[0][0] = 0
    while Q :
        x,y = Q.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if issafe(nx,ny) :
                temp = 0
                if m[ny][nx]-m[y][x] >= 0 :
                    temp = m[ny][nx] - m[y][x]
                if (c[ny][nx] > c[y][x] + temp + 1) :
                    Q.append((nx,ny))
                    c[ny][nx] = c[y][x] + temp + 1

    print("#%d %d"%(tc+1,c[n-1][n-1]))