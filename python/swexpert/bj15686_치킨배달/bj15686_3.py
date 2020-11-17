import sys

sys.stdin = open('bj15686.txt','r')

N,M = map(int,input().split())

homes = []
chickens = []
for i in range(N) :
    item = list(map(int,input().split()))
    for j in range(N) :
        if item[j] == 1 :
            #y,x
            homes.append((i,j))
        elif item[j] == 2 :
            chickens.append((i,j))

def getDistances(home,chicken) :
    return abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])

from itertools import combinations
checkLists = combinations(chickens,M)
res = N*N*N*N
for checkList in checkLists :
    temp = 0
    for home in homes:
        minDis = N*N*N*N
        for chicken in checkList:
            dis = getDistances(home,chicken)
            minDis = dis if dis < minDis else minDis
        temp += minDis
        if temp > res :
            continue
    res = temp if temp < res else res
print(res)
