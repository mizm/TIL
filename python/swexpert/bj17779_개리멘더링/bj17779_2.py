import sys
sys.stdin = open('bj1779.txt','r')

N = int(input())
myMap = []
res = 987654321
for i in range(N) :
    myMap.append(list(map(int,input().split())))

for x in range(1,N) :
    for y in range(1,N) :
        for d1 in range(1,N-1) :
            for d2 in range(1,N-1) :
                if 1<= x < x+d1+d2 < N and 1<= y-d1 < y < y+d2 < N :

                    temp = [[5 for i in range(N)] for i in range(N)]
                    for r in range(N) :
                        for c in range(N) :
                            i = r+1
                            j = c+1
                            t = 0
                            if 1<= i and i  < x+d1 and 1<= j and j <= y :
                                t = 0
                            elif 1<= i and i <= x+d2 and y < j and j <= N :
                                t = 1
                            elif x+d1 <= i and i <= N and 1<= j and j < y-d1+d2 :
                                t = 2
                            elif x+d2 < i and i <= N and y-d1+d2 <= j and j <= N :
                                t = 3
                            else :
                                t = 4
                            temp[r][c] = t
                    y1 = y
                    y2 = y
                    for i in range(1, d1 + d2 + 1):
                        x1 = x + i
                        if i > d1:
                            ls = 1
                        else:
                            ls = -1
                        if i > d2:
                            rs = -1
                        else:
                            rs = 1
                        y1 += ls
                        y2 += rs
                        for j in range(y1, y2 + 1):
                            temp[x1 - 1][j - 1] = 4
                    items = [0] * 5
                    for i in range(N) :
                        for j in range(N) :
                            items[temp[i][j]] += myMap[i][j]
                    res = min(res,max(items) - min(items))
print(res)