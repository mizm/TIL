def dfs(pos,num) :
    global m
    if num == n//2 :
        print(visited)
        sx=0
        sy=0
        for i in range(n) :
            x,y = xy[i]
            if visited[i] :
                sx+=x
                sy+=y
            else :
                sx-=x
                sy-=y
        temp = sx*sx+sy*sy
        if m > temp :
            m = temp
        return
    for i in range(pos+1,n) :
        if not visited[i] :
            visited[i] = 1
            dfs(i,num+1)
            visited[i] = 0
for tc in range(int(input())) :
    m = 80000000001
    n = int(input())
    xy = []
    for i in range(n) :
        xy.append(list(map(int,input().split())))
    item = []
    visited = [0]*n
    dfs(0,0)
    print("#%d %d"%(tc+1,m))