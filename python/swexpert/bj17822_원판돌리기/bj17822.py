import sys

sys.stdin = open('bj17822.txt', 'r')

N,M,T = list(map(int,input().split()))
items = []
orders = []
for i in range(N) :
    t = list(map(int,input().split()))
    items.append(t)
for i in range(T) :
    t = list(map(int,input().split()))
    orders.append(t)
re = 0
def rotation(items, order) :
    x,d,k = order
    for i in range(N):
        if (i + 1) % x == 0 :
            for j in range(k) :
                if d == 0 :
                    #시계방향
                    items[i].insert(0, items[i].pop())
                else :
                    #반시계
                    items[i].append(items[i].pop(0))
    return items
def clear(items) :
    #같은 원판 기준 삭제
    my = []
    cnt = 0
    for i in range(N) :
        t = []
        for j in range(M) :
            left = j - 1 if j - 1 >= 0 else M-1
            right = j + 1 if j + 1 < M else 0
            t.append(1 if items[i][j] > 0 and (items[i][j] == items[i][left] or items[i][j] == items[i][right]) else 0)
        my.append(t)
        cnt += sum(t)
    near = [[0 for i in range(M)] for j in range(N)]
    for i in range(N) :
        inside = i - 1 if i - 1 >= 0 else -1
        outside = i + 1 if i + 1 < N else -1
        for j in range(M) :
            if items[i][j] > 0 :
                if inside != -1 and items[i][j] == items[inside][j] :
                    near[i][j] = 1
                if outside != -1 and items[i][j] == items[outside][j] :
                    near[i][j] = 1
        cnt += sum(near[i])
    if cnt > 0 :
        for i in range(N):
            for j in range(M):
                items[i][j] = 0 if near[i][j] or my[i][j] else items[i][j]
    else :
        total = 0
        c = 0
        for i in range(N):
            for j in range(M):
                total += items[i][j]
                c += 1 if items[i][j] > 0 else 0
        if c == 0 :
            return items
        avr = total / c
        for i in range(N):
            for j in range(M):
                if items[i][j] > 0 and items[i][j] > avr:
                    items[i][j] -= 1
                    continue
                if items[i][j] > 0 and items[i][j] < avr:
                    items[i][j] += 1
    return items
for o in orders :
    rotation(items, o)
    clear(items)
for l in items :
    re += sum(l)
print(re)

