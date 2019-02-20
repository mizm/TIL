graph = [[0]*8 for i in range(8)]
visited = [0]*8
data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

for i in range(len(data)//2) :
    start = data[i*2]
    stop = data[i*2+1]
    graph[start][stop] = 1
    graph[stop][start] = 1


def dfs(pos) :
    global graph,visited
    print(pos)
    visited[pos] = 1
    for i in range(1,8) :
        if graph[pos][i] > 0 and visited[i] == 0 :
            dfs(i)


dfs(1)