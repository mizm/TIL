def makehash(pos,item) :
    # print(item)
    global res
    if item == X :
        res = pos
    if item > X :
        return
    if pos > res :
        return
    if item > 0 :
        if X % item == 0 :
            c[item] = pos
    for i in range(len(enable)) :
        makehash(pos + 1, item * 10 + enable[i])
def dfs(pos,item,k) :
    # print(pos, item)
    global res
    if pos >= res :
        return
    if item > X :
        return
    if item == X :
        if res > pos :
            res = pos
        return
    for k1,v1 in c.items():
        if k1 != 1 :
            dfs(pos+v1+1,item*k1,k1)


for tc in range(int(input())) :
    data = list(map(int,input().split()))
    enable = []
    res = 987654321
    arr_x = []
    c = {}
    for i in range(10):
        if data[i] :
            enable.append(i)
    X = int(input())
    for i in range(len(enable)) :
        if enable[i] :
            makehash(1,enable[i])

    for k,v in c.items():
        # print(k)
        dfs(v,k,k)
    res = -1 if res == 987654321 else res + 1
    print("#%d %d"%(tc+1,res))