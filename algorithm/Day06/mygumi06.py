def dfs(pos):
    global startlist
    if startlist[pos] > 1 :
        startlist[pos] -= 1
        return
    elif startlist[pos] == 1 :
        startlist[pos] -= 1
    if not startlist[pos] :
        startlist[pos] -= 1
        print(pos,end=' ')
    for i in range(1, v + 1):
        if graph[pos][i] == 1 and startlist[i] > 0:
            dfs(i)
for tc in range(10) :
    v, e = list(map(int, input().split()))
    graph = [[0] * (v + 1) for i in range(v + 1)]
    data = list(map(int, input().split()))
    startlist = [0] * (v+1)
    visit = [0] * (v+1)
    for i in range(len(data)//2) :
        start = data[i*2]
        stop = data[i*2+1]
        graph[start][stop] = 1
        startlist[stop] += 1
    print(f'#{tc+1} ',end='')
    for i in range(1,v+1) :
        if startlist[i] == 0 :
            dfs(i)
    print()