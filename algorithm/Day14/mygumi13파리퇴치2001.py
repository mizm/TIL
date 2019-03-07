for a in range(int(input())) :
    t = list(map(int,input().split()))
    m = []
    top = 0
    for j in range(t[0]) :
        m.append(list(map(int,input().split())))
    for i in range(t[0]-t[1]+1) :
        for j in range(t[0]-t[1]+ 1):
            s = 0
            for k in range(t[1]) :
                for p in range(t[1]):
                    s += m[j+k][i+p]
            if top < s :
                top = s
    print('#{} {}'.format((a+1),top))