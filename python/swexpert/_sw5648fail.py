for a in range(int(input())) :
    n = int(input())
    all_xy = []
    MAX_XY = 4002
    MIN_XY = 0
    item = []
    fullmap = [[0 for i in range(4004)] for i in range(4004)]
    checkmap = [[0 for i in range(4004)] for i in range(4004)]
    for i in range(n) :
        x,y,drt,e = list(map(int,input().split()))
        x += 1000
        y += 1000
        x *= 2
        y *= 2
        item.append([x,y,drt,e])
        fullmap[y][x] = 1
    move = [[0,1],[0,-1],[-1,0],[1,0]]
    energy = 0
   
    for i in range(4000) :
        tenergy = 0
        for t in item :
            if t[3] == 0 :
                continue
            m_x,m_y = move[t[2]]
            
            t[0] += m_x
            t[1] += m_y
            if t[0] < 0 or t[0] > 4003 or t[1] < 0 or t[1] > 4003 :
                fullmap[t[1]][t[0]] -= 1
                t[3] = 0
            else :
                #int(t)
                fullmap[t[1]][t[0]] += 1
                checkmap[t[1]][t[0]] = 1
        for t in item :
            if t[3] == 0 :
                continue
            x,y = t[0],t[1]
            if checkmap[y][x] == 1:
                if fullmap[y][x] == 1 :
                    checkmap[y][x] = 0
                else :
                    tenergy += t[3]
                    t[3] = 0
                    fullmap[y][x] -= 1
        energy += tenergy
        cnt = 0
        for t in item :
            if t[3] == 0 :
                cnt += 1
        if cnt == n :
            break
    print(energy)

        
