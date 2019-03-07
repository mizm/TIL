def issafe(x,y,visited) :
    return x >= 0 and x < 100 and y >= 0 and y < 100 and data[y][x] == 1 and not visited[y][x]
# 반복
def search(endx):
    global px,m
    visited = [[0]*100 for i in range(100)]
    endy = 99
    dis = 0
    while endy > 0 :
        visited[endy][endx] = 1
        for i in range(3) :
            if issafe(endx+dx[i],endy+dy[i],visited):
                endx += dx[i]
                endy += dy[i]
                dis+=1
                break
    print(dis)
    if m > dis :
        m = dis
        px = endx
for tc in range(10) :
    m = 100*100*100
    px = -1
    data = []
    dx = [1,-1,0]
    dy = [0,0,-1]
    n = int(input())
    for i in range(100) :
        data.append(list(map(int, input().split())))
    endx = 0
    endy = 99
    for i in range(100) :
        if data[99][i] == 1 :
            endx = i
            search(endx)
    print('#%d %d'%((tc+1),px))

#재귀
# def dfs(x,y) :
#     global data, endx
#     if y == 0 :
#         endx = x
#         return
#     data[y][x] = 0
#     # visited.append((x, y))
#     dx = [1, -1, 0]
#     dy = [0,0,-1]
#     for i in range(3) :
#         if issafe(x + dx[i], y + dy[i]):
#             x += dx[i]
#             y += dy[i]
#             dfs(x,y)
#             break
#
#
#
# for tc in range(10) :
#     data = []
#     n = int(input())
#     for i in range(100) :
#         data.append(list(map(int, input().split())))
#     endx = 0
#     endy = 99
#     for i in range(100) :
#         if data[99][i] == 2 :
#             endx = i
#             break
#     dfs(endx, endy)
#     print(f'#{n} {endx}')
