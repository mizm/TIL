# def dfs(pos,temp) :
#     global my_min
#     if temp > my_min :
#         return
#     if pos >= f :
#         if my_min > temp :
#             my_min = temp
#         return
#     for i in range(pos,pos+p-f+1) :
#         if visited[i] :
#             item = abs(fire[pos]-pump[i])
#             temp += item
#             visited[i] = 0
#             dfs(pos+1,temp)
#             temp -= item
#             visited[i] = 1
#

def search():
    global my_min
    temp = 0
    __fire = _fire[:]
    _visited = visited[:]
    temp1 = 0
    while __fire:
        # if flag :
        #     item = _fire.pop(0)
        # else :
        if my_min < temp1:
           break
        item = __fire.pop()
        i = item
        j = item
        while i > 0:
            i -= 1
            if _visited[i] < 0:
                break
        while j < p + f + 1:
            j += 1
            if _visited[j] < 0:
                break
        t1 = abs(pump[item] - pump[i])
        t2 = abs(pump[item] - pump[j])
        if t1 < t2:
            temp1 += t1
            _visited[i] = 1
        else:
            temp1 += t2
            _visited[j] = 1
    if my_min > temp1 :
        my_min = temp1
    # print(temp1,temp)

#소방차
p,f = map(int,input().split())
pump = list(map(int,input().split()))
fire = list(map(int,input().split()))
_fire = []
visited = [-1] * (p+f+2)

my_min = 98881000000
cnt = 0
flag = True
for i in fire :
    while True :
        if cnt == len(pump) :
            pump.append(i)
            _fire.append(cnt+1)
            visited[cnt+1] = 1
            flag = False
            break
        if i > pump[cnt] :
            cnt += 1
        else :
            pump.insert(cnt,i)
            _fire.append(cnt+1)
            visited[cnt+1] = 1
            cnt+=1
            break
pump.append(98881000000)
pump.insert(0,98881000000)
for i in range(f+1) :
    item = _fire.pop(0)
    search()
    _fire.append(item)
# print(pump)
# print(_fire)

print(my_min)