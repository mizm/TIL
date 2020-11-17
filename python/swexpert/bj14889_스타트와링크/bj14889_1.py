import sys

sys.stdin = open('bj14889.txt', 'r')

from itertools import combinations

N = int(input())
items = []
member = [i for i in range(N)]
mid = N//2
for i in range(N) :
    items.append(list(map(int,input().split())))

member_lists = combinations(member,mid)
res = N*100*100
for first in member_lists :
    second = []
    for m in member :
        if not m in first :
            second.append(m)
        scores = [0,0]
    for i in range(mid) :
        for j in range(i+1,mid) :
            # 앞에팀
            scores[0] += items[first[i]][first[j]]
            scores[0] += items[first[j]][first[i]]
            # 뒤에팀
            scores[1] += items[second[i]][second[j]]
            scores[1] += items[second[j]][second[i]]
    tres = abs(scores[0] - scores[1])
    res = res if res < tres else tres
print(res)