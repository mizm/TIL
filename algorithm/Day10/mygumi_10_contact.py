def bfs(start):
    queue = []
    queue.append(start)
    distance = [0]*101
    while queue :
        item = queue.pop(0)
        for i in range(101) :
            if my_map[item][i] > 0 and distance[i] == 0:
                queue.append(i)
                distance[i] = distance[item] + 1
    print(distance)
    # print(distance[item])
    for i in range(101) :
        if distance[100-i] == distance[item] :
            return 100-i
def dfs(start) :
    global max_dis
    for i in range(1,101) :
        if my_map[start][i] > 0 and not visited[i]:
            visited[i] = start
            if distance[i] > 0 :
                if distance[i] > distance[start] + 1 :
                    distance[i] = distance[start] + 1
            else :
                distance[i] = distance[start] +1
            # if distance[i] > distance[start] + 1 :
            #     distance[i] = distance[start]+1
            dfs(i)
            visited[i] = 0


for tc in range(10) :
    n,start = map(int,input().split())
    my_map = [[0] *101 for i in range(101)]
    final = 0
    data = list(map(int,input().split()))
    distance = [0]*101
    max_dis = 0
    pos = 0
    visited = [0]*101
    for i in range(n//2) :
        f,t = data[i*2],data[i*2+1]
        my_map[f][t] = 1
    # print(f'#{tc+1} {bfs(start)}')
    distance[start] = 0
    dfs(start)
    #
    # print(max_dis)
    # print(distance)
    for i in range(101):
        if distance[100 - i] > max_dis :
            max_dis = distance[100-i]
            pos = 100-i
    print
    print(f'#{tc+1} {pos}')