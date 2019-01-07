def chk(l) :
    for i in range(1,10) :
        if not l.count(i) == 1:
            return 1
    return 0
for i in range(int(input())) :
    m = [] #가로
    r = [] #네모
    k = [] #세로
    for t in range(9):
        k.append([])
        r.append([])
    for j in range(9) :
        m.append(list(map(int,input().split())))
        for t in range(9) :
            k[t].append(m[j][t])
            r[t//3+j//3].append(m[j][t])
    for j in range(9) :
        if chk(k[j]) or chk(r[j]) or chk(m[j]) :
            print(f'#{i+1} 0')
            break
        else :
            print(f'#{i+1} 1')
            break