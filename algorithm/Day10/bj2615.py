#오목
def bfs(data,flag) :
    n = len(data)
    visited = [0]*n
    for i in range(n) :
        if visited[i] == 0 :
            chk = 0
            x2,y2 = data[i]
            x1,y1 = data[i]
            visited[i] = 1
            while True :
                # print(dx[flag*2])
                newx = x1+dx[flag*2]
                newy = y1+dy[flag*2]
                if (newx,newy) in data:
                    chk += 1
                    x1 = newx
                    y1 = newy
                    visited[data.index((newx,newy))] = 1
                else : break
            while True :
                newx2 = x2+dx[flag*2 +1]
                newy2 = y2+dy[flag*2 +1]
                if (newx2, newy2) in data :
                    chk += 1
                    x2 = newx2
                    y2 = newy2
                    visited[data.index((newx2, newy2))] = 1
                else : break
            if chk == 4 :
                return (newy2-dy[flag*2 +1]+1,newx2-dx[flag*2 +1]+1)
    return False




# def set
my_map = []
n = 19
black = []
white = []
for i in range(n) :
    temp = input().split()
    for j in range(n) :
        if temp[j] == "1" :
            white.append((j, i))
        elif temp[j] == "2" :
            black.append((j, i))

# for i in range(n) :
#     for j in range(n) :
#         if my_map[i][j] == 1 :
#             white.append((j,i))
#         elif my_map[i][j] == 2 :
#             black.append((j,i))

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]
chk = 1
for i in range(4) :
    item = bfs(white,i)
    if item :
        print(1)
        print(item[0],item[1])
        chk = 0
        break
    item = bfs(black,i)
    if item :
        print(2)
        print(item[0],item[1])
        chk = 0
        break
if chk :
    print(0)
# bfs(white,2)

# print((2,3) in white)