def star(n, x, y) :
    if n == 3 :
        m[y][x] = '*'
        m[y+1][x-1] = '*'
        m[y+1][x+1] = '*'
        for i in range(x-2,x+3) :
            m[y+2][i] = '*'
    else :
        star(n//2, x - n//2, y + n//2)
        star(n//2, x + n//2, y + n//2)
        star(n//2, x, y)
n = int(input())
m = []
for i in range(n) :
    m.append([' ' for i in range(2*n-1)])
star(n,n-1,0)
for i in m :
    print(''.join(i))
