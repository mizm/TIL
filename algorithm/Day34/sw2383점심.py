def timec(bincase,person,floor,floorList) :
    time = 0
    AList , BList = floorList[0] , floorList[1]
    A,B=floor[0],floor[1]
    state = []
    for i in range(len(bincase)) :
        if bincase[i] == '1':
            state.append(abs(A[0] - person[i][0]) + abs(A[1] - person[i][1])+1)
        else :
            state.append(abs(B[0] - person[i][0]) + abs(B[1] - person[i][1])+1)
    fin = len(state) + len(AList) + len(BList)
    chkfin = 0
    while chkfin < fin :
        chkfin = 0
        for i in state :
            if i == -1 :
                chkfin += 1
        for i in AList :
            if i == 0 :
                chkfin += 1
        for i in BList :
            if i == 0 :
                chkfin += 1
        if chkfin >= fin :
            break
        for i in range(len(state)) :
            if state[i] > 0 :
                state[i] -= 1
        if 0 in state :
            checkA = checkB = 0
            del AList[0]
            del BList[0]
            time += 1
            for i in range(len(state)) :
                if state[i] == 0 :
                    if bincase[i] == '1':
                        if sum(AList) + checkA < 3 :
                            state[i] = -1
                            checkA+=1
                        else :
                            continue
                    else :
                        if sum(BList) + checkB < 3 :
                            state[i] = -1
                            checkB+=1
                        else :
                            continue
            AList.append(checkA)
            BList.append(checkB)
            continue
        else :
            AList.append(0)
            del AList[0]
            BList.append(0)
            del BList[0]
        time += 1
    return time
for a in range(int(input())):
    n =int(input())
    allmap=[list(map(int,input().split())) for i in range(n)]
    person = []
    floorList = []
    floor = []
    for x in range(n) :
        for y in range(n) :
            temp = allmap[x][y]
            if temp == 1 :
                person.append((x,y))
            elif temp > 1 :
                floorList.append([0 for i in range(temp)])
                floor.append((x,y))
    t = 2**len(person)
    m = k = 100
    for i in range(t) :
        k = timec(bin(i)[2:].zfill(len(person)),person,floor,floorList)
        if m >= k:
            m = k
    print('#{a+1} {m}')