n, r1, r2 = list(map(int,input().split()))

graph = [{} for x in range(n)]
selected_graph = [1 for x in range(n)]
dis_graph = [0 for x in range(n)]
queue = []
min_dis = 789456
for i in range(n-1) :
    start,end,dis = list(map(int,input().split()))
    graph[start-1].update({end-1:dis})
    graph[end-1].update({start-1:dis})
queue.append(r1)
while len(queue) != 0 :
    item = queue.pop(0)-1
    if item == r2-1 :
        break
    # if item == end:
    #     print(queue)
    selected_graph[item] = 0
    for k,v in graph[item].items() :
        if selected_graph[k] :
            dis_graph[k] = item+1
            queue.append(k+1)
r_sum = 0
r_max = 0
while r2 != r1 :
    temp = graph[r2 - 1][dis_graph[r2 - 1] - 1]
    if r_max < temp :
        r_max = temp
    r_sum += temp
    r2 = dis_graph[r2 - 1]
print(r_sum-r_max)

