def issafe(x,y) :
    return x >= 0 and x < m and y >= 0 and y < n and my_map[y][x] >= 0

def search():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    queue = [(0,0)]
    time = 0
    chk = 1
    while chk :
        queue = [(0, 0)]
        time += 1
        while queue :

            x,y = queue.pop(0)
            my_map[y][x] = -1
            for i in range(4) :
                newx = x + dx[i]
                newy = y + dy[i]
                if issafe(newx,newy) :
                    if my_map[newy][newx] == 1 :
                        my_map[newy][newx] = -2
                    elif my_map[newy][newx] == 0 :
                        my_map[newy][newx] = -1
                        queue.append((newx, newy))
        chk = 0
        cnt = 0
        for j in range(n) :
            for i in range(m) :
                if my_map[j][i] == -1 :
                    my_map[j][i] = 0
                elif my_map[j][i] == -2 :
                    cnt += 1
                    my_map[j][i] = 0
                elif my_map[j][i] == 1:
                    chk += 1
    print(time,cnt)
my_map = []
n,m = map(int,input().split())
for i in range(n) :
    my_map.append(list(map(int,input().split())))
search()
# for i in my_map :
#     print(i)