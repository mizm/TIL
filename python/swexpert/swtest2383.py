def timec(bincase,person,floor,floorList) :
    time = 0
    AList , BList = floorList[0] , floorList[1]
    A,B=floor[0],floor[1]
    while True :
        


        time += 1
    return time
for a in range(int(input())):
    n =int(input())
    allmap=[list(map(int,input().split())) for i in range(n)]
    # person = [(x,y) for x in range(n) for y in range(n) if allmap[x][y]==1]
    # floor = [(x,y) for x in range(n) for y in range(n) if allmap[x][y] > 1]
    # 사람위치,계단 리스트 추가
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
    #==               
    t = 2**len(person)
    m = k = t
    for i in range(t) :
        k = timec(bin(i)[2:],person,floor,floorList)
        if m <= k:
            m = k