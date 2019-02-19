for tc in range(int(input())) :
    n = int(input())
    color1 = []
    color2 = []
    for i in range(n) :
        x1,y1,x2,y2,c = list(map(int,input().split()))
        for i in range(x1,x2+1) :
            for j in range(y1,y2+1) :
                if c == 1 :
                    if not (i,j) in color1 :
                        color1.append((i,j))
                elif c == 2:
                    if not (i,j) in color2 :
                        color2.append((i,j))
    result = 0
    for i in color1 :
        if i in color2 :
            result += 1
    print(f'#{tc+1} {result}')