for a in range(int(input())) :
    n = int(input())
    item = []
    for i in range(n) :
        x,y,drt,e = list(map(int,input().split()))
        x += 1000
        y += 1000
        x *= 2
        y *= 2
        item.append([x,y,drt,e])
    move = [[0,1],[0,-1],[-1,0],[1,0]]
    energy = 0
    for i in range(4004) :
        check = {}
        
        for t in item :
            if t[3] == 0:
                continue
            m_x,m_y = move[t[2]]
            next_x = t[0]+m_x
            next_y = t[1]+m_y
            if next_x >= 0 and next_x <= 4004 and next_y >= 0 and next_y <= 4004 :
                if not check.get((next_x,next_y)) :
                    check[(next_x,next_y)] = 1
                else :
                    check[(next_x,next_y)] = check[(next_x,next_y)] + 1
                t[0] = next_x
                t[1] = next_y
            else :
                t[3] = 0
        tempe = 0
        for t in item :
            if t[3] == 0 :
                continue
            if check[(t[0],t[1])] > 1 :
                tempe += t[3]
                t[3] = 0
        energy += tempe
        cnt = 0
        for t in item :
            if t[3] == 0 :
                cnt += 1
        if cnt == n :
            break
    print(f'#{a+1} {energy}')