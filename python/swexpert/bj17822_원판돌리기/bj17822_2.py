import sys

sys.stdin = open('bj17822.txt', 'r')

N,M,T = map(int,input().split())
CNT = 0
circles = []
for _ in range(N) :
    circles.append(list(map(int,input().split())))
CNT = len(circles[0])
def go(d,circle, k) :
    for _ in range(k) :
        if d == 0 :
            circle.insert(0,circle.pop())
        else :
            p = circle.pop(0)
            circle.append(p)
    return circle

for _ in range(T) :
    x,d,k = map(int,input().split())
    # 돌리고 돌리고고
    for i in range(N) :
        if (i + 1) % x == 0 :
            go(d,circles[i],k)
    # 제거하자
    delList = []
    allSum = 0
    cnt = 0
    for i in range(N) :
        for j in range(CNT) :
            if circles[i][j] == 0 :
                continue
            if circles[i][j-1 if j > 0 else CNT-1] == circles[i][j] or circles[i][j+1 if j < CNT-1 else 0] == circles[i][j] :
                delList.append((i,j))
                continue
            if 0 < i < N - 1:
                if circles[i-1][j] == circles[i][j] or circles[i+1][j] == circles[i][j] :
                    delList.append((i,j))
                    continue
            if i == 0 :
                if circles[i+1][j] == circles[i][j] :
                    delList.append((i,j))
                    continue
            if i == N-1 :
                if circles[i-1][j] == circles[i][j] :
                    delList.append((i,j))
                    continue
            allSum += circles[i][j]
            cnt += 1
    if delList :
        for y,x in delList :
            circles[y][x] = 0
    else :
        if allSum == 0 :
            break
        # 평균 -> 변경
        e = allSum/cnt
        for i in range(N):
            for j in range(CNT):
                if circles[i][j] == 0:
                    continue
                if circles[i][j] < e :
                    circles[i][j] += 1
                elif circles[i][j] > e :
                    circles[i][j] -= 1
res = 0
for _ in range(N) :
    res += sum(circles[_])
print(res)
