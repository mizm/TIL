import sys

sys.stdin = open('bj16235.txt','r')

N,M,K = map(int,input().split())
originMap = []
energy = []
treeCnt = 0
trees = [[[] for i in range(N)] for j in range(N)]
for i in range(N) :
    originMap.append([5 for _ in range(N)])
    energy.append(list(map(int,input().split())))

#M개 심음
#4계절
for i in range(M) :
    y,x,age = map(int,input().split())
    trees[y-1][x-1].append(age)
    treeCnt += 1
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
for t in range(K) :
    #봄에는 양분을 먹자
    dies = []
    for y in range(N) :
        for x in range(N) :
            if trees[y][x] :
                item = trees[y][x]
                item.sort()
                live = []
                for j in range(len(item)):
                    if originMap[y][x] >= item[j]:
                        originMap[y][x] -= item[j]
                        live.append(item[j] + 1)
                    else:
                        treeCnt -= 1
                        dies.append((x, y, int(item[j] / 2)))
                trees[y][x] = live
    #여름
    for x,y,e in dies :
        originMap[y][x] += e
    #가을
    sexTree = []
    for y in range(N) :
        for x in range(N) :
            if trees[y][x]:
                for age in trees[y][x] :
                    if age % 5 == 0 :
                        for j in range(8):
                            if 0 <= x + dx[j] < N and 0 <= y + dy[j] < N:
                                trees[y + dy[j]][x + dx[j]].append(1)
                                treeCnt += 1
    #겨울
    for i in range(N) :
        for j in range(N) :
            originMap[i][j] += energy[i][j]
print(treeCnt)


