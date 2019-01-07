for a in range(int(input())) :
    n = int(input())
    m = []
    for i in range(n) :
        m.append([0 for i in range(n)])
    x=y=0
    s=0
    for j in range(n*n) :
        m[x][y]=j+1
        if s == 0 :
            if y + 1 >= n or m[x][y+1] > 0:
                s=1
                x+=1
            else :
                y+=1
        elif s == 1:
            if x + 1 >= n or m[x+1][y] > 0:
                s=2
                y-=1
            else :
                x+=1
        elif s == 2:
            if y-1 < 0 or m[x][y-1] > 0:
                s=3
                x-=1
            else :
                y-=1
        elif s == 3:
            if x-1< 0 or m[x-1][y] > 0:
                s=0
                y+=1
            else :
                x-=1     
    print(f'#{a+1}')
    for j in m :
        print(' '.join(map(str,j)))