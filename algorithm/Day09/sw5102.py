for tc in range(int(input())) :
    v,e = list(map(int,input().split()))
    my_map = {}
    distance = [0]*(v+1)
    # parent = [0]*(v+1)
    queue = [0]*(v*v)
    front = rear = -1
    for i in range(e) :
        s,g = list(map(int,input().split()))
        if my_map.get(s) :
            my_map[s].append(g)
        else :
            my_map.update({s:[g]})
        if my_map.get(g):
            my_map[g].append(s)
        else:
            my_map.update({g: [s]})
    s,g = list(map(int,input().split()))
    rear += 1
    queue[rear] = s
    while front <= rear :
        front += 1
        item = queue[front]
        if item == 0 :
            break
        for i in my_map[item] :
            if distance[i] <= 0 :
                rear += 1
                queue[rear] = i
                # parent[i] = item
                distance[i] = distance[item] + 1
    print(f'#{tc+1} {distance[g]}')
