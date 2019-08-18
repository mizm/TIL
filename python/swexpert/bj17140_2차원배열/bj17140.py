import sys

sys.stdin = open('bj17140.txt', 'r')

r,c,k = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(3)]
r-=1
c-=1
res = -1

def check(r,c,k) :
    global A
    if A[r][c] == k :
        return True
    maxcolumn= 3
    for i in range(3) :
        if maxcolumn < len(A[i]) :
            maxcolumn = len(A[i])



res = -1
for i in range(0,101) :
    if check(r,c,k) :
        res = i
        break
print(res)