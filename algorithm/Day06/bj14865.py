item = []
temp = []
cnt = 0
idx = 0
for i in range(int(input())) :
    x,y = list(map(int, input().split()))
    if y < 0 :
        y = 0

    if not x in temp :
        if y == 0 and cnt == 0:
            temp.append(x)
            cnt += 1
        elif y == 0 and cnt == 1 :
            if temp[0] > x :
                temp.insert(0,x)
            else :
                temp.append(x)
            cnt += 1
    if cnt == 2 :
        item.append((temp[0],temp[1]))
        cnt = 0
        idx += 1
        temp = []
# print(item)
# item = [(0,1),(2,7),(3,4),(5,6),(8,9)]
n = len(item)
include = 0
notinclude = 0
visit = [1]*n
item = sorted(item)
# print(item)

for i in range(n) :
    if visit[i] :
        visit[i] = 0
        include += 1
        notinclude += 1
    else :
        continue
    if i < n-1 :
        if item[i][1] < item[i+1][0] :
            notinclude += 1
            continue
    k = 0
    for j in range(i+1,n) :
        if item[i][0] < item[j][0] :
            include += 1
            k = 1
            visit[j] = 0
    if k :
        include -=1
print(notinclude, include)
