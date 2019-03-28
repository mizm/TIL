def checkmin():
    item =MAXVALUE
    idx = -1
    for i in range(len(distance)) :
        if distance[i] < item and not i in idx_list:
            item = distance[i]
            idx = i
    return idx

for tc in range(int(input())):
    n,e = map(int,input().split())
    MAXVALUE = 987654321
    my_map = [[MAXVALUE]*(n) for i in range(n)]
    for i in range(e) :
        to,fr, = map(int,input().split())
        my_map[to-1][fr-1] = 1
        my_map[fr - 1][to - 1] = 1
    idx_list = [0]
    distance = my_map[0][:]
    while len(idx_list) < len(distance) :
        t = checkmin()
        idx_list.append(t)
        for i in range(len(distance)) :
            if not i in idx_list :
                # distance[i] = min(distance[i] , my_map[t][i] + distance[t])
                if my_map[t][i] + distance[t] < distance[i] :
                    # parent[i] = t
                    distance[i] = my_map[t][i] + distance[t]
    cnt = 0
    # print(distance)
    # for i in distance :
    #     if i <= 2 :
    #         cnt += 1
    print("#%d %d"%(tc+1,distance.count(1)+distance.count(2)))