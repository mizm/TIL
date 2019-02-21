def dfs(a,b) :
    global item,cnt
    k = n//10
    a = a//10
    b = b//10

    ca = cb = -1
    for i in range(k) :
        if item[0][i] == 0 :
            ca = 0
            cb = i
            break
        if item[1][i] == 0 :
            ca = 1
            cb = i
            break
    if ca + a > 2 :
        return
    if cb + b > k :
        return
    for i in range(a):
        for j in range(b) :
            item[ca+i][cb+j] = 1
    check = True
    for i in range(k) :
        if item[0][i] == 0 or item[1][i] == 0 :
            check = False
            break
    if check :
        cnt += 1
        for i in range(a):
            for j in range(b):
                item[ca + i][cb + j] = 0
        return
    dfs(10,20)
    dfs(20,10)
    dfs(20,20)
    for i in range(a):
        for j in range(b):
            item[ca + i][cb + j] = 0




for tc in range(int(input())) :
    cnt = 0
    n = int(input())
    item = [[0]*(n//10) for i in range(2)]
    dfs(10, 20)
    dfs(20, 10)
    dfs(20, 20)
    print(cnt)