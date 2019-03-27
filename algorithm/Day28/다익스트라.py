MAXVALUE = 987654321

my_map = [[MAXVALUE]*6 for i in range(6)]

k,n = map(int,input().split())
for i in range(n) :
    to,fr,dis = map(int,input().split())
    my_map[to][fr] = dis
distance = my_map[0][:]
parent = [0]*6
def checkmin():
    item =MAXVALUE
    idx = -1
    for i in range(len(distance)) :
        if distance[i] < item and not i in idx_list:
            item = distance[i]
            idx = i
    return idx

idx_list = [0]
while len(idx_list) < len(distance) :
    t = checkmin()
    idx_list.append(t)
    for i in range(len(distance)) :
        if not i in idx_list :
            # distance[i] = min(distance[i] , my_map[t][i] + distance[t])
            if my_map[t][i] + distance[t] < distance[i] :
                parent[i] = t
                distance[i] = my_map[t][i] + distance[t]

print(distance)
print(parent)
