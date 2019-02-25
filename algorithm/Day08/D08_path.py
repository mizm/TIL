def path(pos) :
    global my_min, visted
    k = sum(visited)
    if my_min < k :
        return
    if pos == v :
        if my_min > k :
            my_min = k

    for i in range(1,v+1) :
        if my_graph[pos][i] > 0 :
            visited[i] = my_graph[pos][i]
            path(i)
            visited[i] = 0


v, e = list(map(int, input().split()))
my_graph = [[0]*(v+1) for i in range(v+1)]
visited = [0]*(v+1)
visited[1] = 1
my_min = 0
for i in range(e) :
    start,end,cost = list(map(int, input().split()))
    my_graph[start][end] = cost
    my_min += cost
check = False
for i in range(1,e+1) :
    if my_graph[i][e] > 0 :
        check = True
        break
if check :
    path(1)
    print(my_min-1)
else :
    print(-1)