import sys

sys.stdin = open('bj15686.txt','r')
import itertools
N,M = map(int,input().split())

houses = []
chicken = []

for i in range(N) :
    temp = list(map(int,input().split()))
    for j in range(N) :
        if temp[j] == 1 :
            # house
            houses.append((j,i))
        elif temp[j] == 2 :
            chicken.append((j,i))

it = itertools.combinations(chicken,M)
res =987654321
def getDistance(c,h,res) :
    small = 0
    for x1,y1 in h :
        t = 987654321
        for x2,y2 in c :
            dis = abs(x1-x2) + abs(y1-y2)
            if t > dis :
                t = dis
        small += t
        if small > res :
            break
    return small
for k in it:
    kres = getDistance(k,houses,res)
    if res > kres :
        res = kres

print(res)