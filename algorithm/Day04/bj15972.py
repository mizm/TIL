class box :
    def __init__(self,h):
        self.up = -1
        self.down = -1
        self.right = -1
        self.left = -1
        self.h = h
    def set_up(self,x):
        self.up = x
    def set_down(self,x):
        self.down = x
    def set_right(self,x):
        self.right = x
    def set_left(self,x):
        self.left = x
    def __str__(self):
        return (f'up {self.up} down {self.down} right {self.right} left {self.left} h {self.h}')
def issafe(x,y,n,m) :
    return x >= 0 and x < n and y >= 0 and y < m
n, m, h = list(map(int, input().split()))
hole = [[box(h) for i in range(m)] for j in range(n)]
for i in range(n+1) :
    temp = list(map(int, input().split()))
    for j in range(len(temp)) : #구멍에 대한 정보를 저장해봅시다
        if i < n:
            hole[i][j].set_up(temp[j])
        if i > 0 :
            hole[i-1][j].set_down(temp[j])
for i in range(n) :
    temp = list(map(int, input().split()))
    for j in range(len(temp)) :
        if j < m :
            hole[i][j].set_left(temp[j])
        if j > 0 :
            hole[i][j-1].set_right(temp[j])
# for i in range(n) :
#     for j in range(m) :
#         if i == 0 :
#             if hole[i][j].up != -1 :
#                 hole[i][j].h = hole[i][j].up
#         if i == n-1 :
#             if hole[i][j].down != -1 :
#                 hole[i][j].h = hole[i][j].down
#         if j == 0 : # left
#             if hole[i][j].left != -1 :
#                 hole[i][j].h = hole[i][j].left
#         if j == m-1 : #right
#             if hole[i][j].right != -1 :
#                 hole[i][j].h = hole[i][j].right

dx = [-1,0,1,0]
dy = [0,1,0,-1]
check = True
while check :
    tempHigh = [[hole[j][i].h for i in range(m)] for j in range(n)]
    print(tempHigh)
    for i in range(n) :
        for j in range(m) :
            if i == 0:
                if hole[i][j].up != -1 and hole[i][j].h > hole[i][j].up:
                    hole[i][j].h = hole[i][j].up
                    continue
            if i == n - 1:
                if hole[i][j].down != -1 and hole[i][j].h > hole[i][j].down:
                    hole[i][j].h = hole[i][j].down
                    continue
            if j == 0:  # left
                if hole[i][j].left != -1 and hole[i][j].h > hole[i][j].left:
                    hole[i][j].h = hole[i][j].left
                    continue
            if j == m - 1:  # right
                if hole[i][j].right != -1 and hole[i][j].h > hole[i][j].right:
                    hole[i][j].h = hole[i][j].right
                    continue
            for k in range(4) :
                nowhigh = hole[i][j].h
                if issafe(i+dx[k], j+dy[k], n, m) :
                    if k == 0 : # up
                        up = hole[i][j].up
                        if up > -1 :
                            if hole[i+dx[k]][j+dy[k]].h < nowhigh and nowhigh > up:
                                next = hole[i+dx[k]][j+dy[k]].h
                                if next >= up :
                                    hole[i][j].h = next
                                else :
                                    hole[i][j].h = up
                                # hole[i + dx[k]][j + dy[k]].h += next
                                # break
                    elif k == 1 :
                        right = hole[i][j].right
                        if right > -1:
                            if hole[i + dx[k]][j + dy[k]].h < nowhigh and nowhigh > right:
                                next = hole[i+dx[k]][j+dy[k]].h
                                if next >= right :
                                    hole[i][j].h = next
                                else:
                                    hole[i][j].h = right
                                # hole[i][j].h -= hole[i+dx[k]][j+dy[k]].h
                                # hole[i + dx[k]][j + dy[k]].h += next
                                # break
                    elif k == 2:
                        down = hole[i][j].down
                        if down > -1:
                            if hole[i + dx[k]][j + dy[k]].h < nowhigh and nowhigh > down:
                                next = hole[i + dx[k]][j + dy[k]].h
                                if next >= down :
                                    hole[i][j].h = next
                                else :
                                    hole[i][j].h = down

                                # hole[i][j].h -= hole[i+dx[k]][j+dy[k]].h
                                # hole[i + dx[k]][j + dy[k]].h += next
                                # break
                    elif k == 3 :
                        left = hole[i][j].left
                        if left > -1:
                            if hole[i + dx[k]][j + dy[k]].h < nowhigh and nowhigh > left:
                                next = hole[i+dx[k]][j+dy[k]].h
                                if next >= left :
                                    hole[i][j].h = next
                                else :
                                    hole[i][j].h = left
                                # hole[i][j].h -= hole[i+dx[k]][j+dy[k]].h
                                # hole[i + dx[k]][j + dy[k]].h += next
                                # break
    check = False
    for i in range(n) :
        for j in range(m) :
            if tempHigh[i][j] != hole[i][j].h :
                check = True
                break
# for i in range(n) :
#     for j in range(m) :
#         print(hole[i][j])
#     print()

result = 0
for i in tempHigh :
    result += sum(i)
print(result)