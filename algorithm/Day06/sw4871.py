def dfs(pos) :
    print(pos)
    for i in range(1,v+1) :
        if graph[pos][i] == 1 :
            graph[pos][i] = 2
            dfs(i)

for tc in range(int(input())) :
    v,e = list(map(int, input().split()))
    graph = [[0] * (v+1) for i in range(v+1)]

    for i in range(e):
        a,b = list(map(int, input().split()))
        graph[a][b] = 1
    start, end = list(map(int, input().split()))
    # for i in graph :
    #     print(i)
    visited = []
    result = 0
    dfs(start)
    print(f'#{tc+1} {result}')