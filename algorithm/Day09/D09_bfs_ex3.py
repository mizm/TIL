def bfs(start) :
    queue = []
    queue.append(start)
    while len(queue) > 0 :
        pa = queue.pop(0)
        print(pa)
        for i in range(1,v+1) :
            if my_graph[pa][i] > 0 and parent[i] < 0 :
                parent[i] = pa
                distance[i] = distance[pa] + 1
                queue.append(i)
v = 7
my_graph = [[0]*(v+1) for i in range(v+1)]
distance = [v*v]*(v+1)
distance[1] = 0
parent = [-1]*(v+1)
parent[1] = 0
data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
for i in range(len(data) // 2):
    start = data[i * 2]
    stop = data[i * 2 + 1]
    my_graph[start][stop] = 1
    my_graph[stop][start] = 1
bfs(1)
print(parent)
print(distance)