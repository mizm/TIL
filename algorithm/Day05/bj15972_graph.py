n, m, h = list(map(int, input().split()))
graph = [{} for i in range(n*m+1)]
ans = [h for i in range(n*m+1)]
select = [1 for i in range(n*m+1)]
def edge(graph,a,b,w) :
    if graph[a].get(b,99999) > w :
        graph[a].update({b:w})
    if graph[b].get(a, 99999) > w:
        graph[b].update({a:w})
for i in range(n+1) :
    temp = list(map(int, input().split()))
    for j in range(m) :
        if temp[j] == -1 : continue
        if i == 0:
            # print(i*m+j+1)
            edge(graph, i*m+j+1, 0, temp[j])
        elif i >= n :
            edge(graph, (i-1)*m+j+1,0,temp[j])
        else :
            edge(graph, i*m+j+1,(i-1)*m+j+1, temp[j])
for i in range(n) :
    temp = list(map(int, input().split()))
    for j in range(len(temp)) :
        if temp[j] == -1 : continue
        # print(i * m + j + 1)
        if j == 0:
            edge(graph, i*m+j+1, 0, temp[j])
        elif j >= m :
            edge(graph, i*m+j,0,temp[j])
        else :
            edge(graph, i*m+j,i*m+1+j, temp[j])
ans[0] = 0
# print(graph)
for k,v in graph[0].items() :
    ans[k] = v

start = sorted(graph[0], key= lambda k : graph[0][k])
# print(start)
# print(graph[0])
for k in start :
    queue = []
    queue.append(k)
    select = [1 for i in range(n * m + 1)]
    while len(queue) :
        item = queue.pop(0)
        select[item] = 0
        for k,v in graph[item].items() :
            # if item == 4 :
            #     print(ans[k],v,k)
            if ans[item] > max(ans[k], v) :
                ans[item] = max(ans[k], v)
            if select[k] :
                queue.append(k)
    # print(item)
    # print(ans[1:])
print(ans[1:])
print(sum(ans[1:]))