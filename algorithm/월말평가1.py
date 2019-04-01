import collections
def issafe(y,x):
    global N
    if y>=0 and x>=0 and y<N and x<N:
        return True
    else:
        return False


dy=[-3,-2,2,3,3,2,-2,-3]
dx=[2,3,3,2,-2,-3,-3,-2]
T=int(input())
for t in range(T):
    N=int(input())
    total_map=[[0]*N for i in range(N)]
    startx,starty,endx,endy=map(int,input().split())
    queue=collections.deque([((starty,startx),0)])
    result=0
    while queue!=[]:
        start=queue.popleft()
        y=start[0][0]
        x=start[0][1]
        if y==endy and x==endx:
            result=start[1]
            break
        for i in range(8):
            if issafe(y+dy[i],x+dx[i]) and total_map[y+dy[i]][x+dx[i]]==0:
                queue.append(((y+dy[i],x+dx[i]),start[1]+1))
                total_map[y + dy[i]][x + dx[i]] = 1
    print('#{} {}'.format(t+1,result))

# 3
# 10
# 0 1 8 4
# 10
# 0 0 2 3
# 10
# 4 4 3 3