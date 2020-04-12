import sys

sys.stdin = open('bj17825.txt', 'r')

dices = [0,0,0,0]
re = 0
items  = list(map(int,input().split()))
map = {
    -1 : [0],
    0 : [0,1],
    1 : [2,2],
    2 : [4,3],
    3 : [6, 4],
    4 : [8, 5],
    5 : [10, 6, 26],
    6 : [12, 7],
    7 : [14, 8],
    8 : [16, 9],
    9 : [18, 10],
    10 : [20, 11,25],
    11 : [22, 12],
    12 : [24,13],
    13 : [26, 14],
    14 : [28, 15],
    15: [30, 16, 31],
    16: [32, 17],
    17: [34, 18],
    18 : [36, 19],
    19 : [38, 20],
    20 : [40, -1],
    26 : [13,27],
    27 : [16,28],
    28 : [19,23],
    23 : [25,22],
    22 : [30,21],
    21 : [35,20],
    25 : [22,24],
    24 : [24,23],
    31 : [28,30],
    30 : [27,29],
    29 : [26,23]
}
def dfs(dices, point, cnt ) :
    global re,items
    if cnt > 9 :
        if point > re:
            re = point
        return
    for d in range(4) :
        if dices[d] == -1 :
            continue
        else :
            #가봐야함.
            ori = dices[d]
            go = dices[d]
            k = items[cnt]
            if len(map.get(go)) > 2 :
                go = map.get(go)[2]
                k-=1
            for i in range(k) :
                go = map.get(go)[1]
                if go == -1 :
                    break
            if go != -1 and go in dices :
                # print(d,ori,go,items[cnt],dices)
                continue
            dices[d] = go
            dfs(dices,point+map.get(go)[0],cnt+1)
            dices[d] = ori
dices[0] = items[0]
dfs(dices,map.get(items[0])[0],1)
print(re)





