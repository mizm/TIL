def searchrangesum(yline,xline1,xline2):
    global M
    result=[]
    for i in range(3):
        if i==0:
            xstart=0
            xend=xline1
        elif i==1:
            xstart=xline1
            xend=xline2
        else:
            xstart=xline2
            xend=M
        rangesum=0
        for y1 in range(0,yline):
            # print(total_map[y1][xstart:xend])
            rangesum+=sum(total_map[y1][xstart:xend])
        result.append(rangesum)

    for i in range(3):
        if i==0:
            xstart=0
            xend=xline1
        elif i==1:
            xstart=xline1
            xend=xline2
        else:
            xstart=xline2
            xend=M
        rangesum=0
        for y2 in range(yline, N):
            # print(total_map[y2][xstart:xend])
            rangesum += sum(total_map[y2][xstart:xend])
        result.append(rangesum)
        # print(result)
    return nodfs(result)
def nodfs(data):
    absolsum=0
    for one in range(4):
        for two in range(one+1,5):
            for three in range(two+1,6):
                absolsum=max(abs(data[one]-data[two])+abs(data[one]-data[three])+abs(data[two]-data[three]),absolsum)
    return absolsum







T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    total_map=[]
    for n in range(N):
        data=list(map(int,input().split()))
        total_map.append(data)
    absolsumresult=[0]
    for yline in range(1,N):
        for xline1 in range(1,M-1):
            for xline2 in range(xline1+1,M):
                # print(yline,xline1,xline2)
                absolsumresult.append(searchrangesum(yline,xline1,xline2))
    print('#{} {}'.format(t+1,max(absolsumresult)))
# 3
# 3 8
# 1 3 8 4 -3 -3 5 1
# 8 -2 5 5 4 -9 -8 -1
# 4 9 2 -1 0 4 3 2
# 3 8
# 4 0 1 -9 9 6 -5 -5
# 2 10 -8 6 9 -10 -3 0
# 9 5 -10 10 -9 -6 2 -8
# 3 8
# -10 -5 8 1 -10 -3 -10 4
# 4 3 9 -6 -4 2 -3 -9
# -4 7 10 3 1 5 9 1