import sys
sys.stdin = open('최소생산비용.txt','r')
def dfs(pos,item) :
    global my_min
    # print(item,my_min)
    if item >= my_min :
        return
    if pos >= n :
        if item < my_min :
            my_min = item
            # print(my_min)
        return
    for i in range(n) :
        if data[i] == 0 :
            data[i] = 1
            dfs(pos+1,item+ma[i][pos])
            data[i] = 0
for tc in range(int(input())) :
    n = int(input())
    ma = []
    for i in range(n) :
        ma.append(list(map(int,input().split())))
    data = [0]*n
    my_min = 987654321
    dfs(0,1)
    print("#%d %d" % (tc + 1, my_min-1))