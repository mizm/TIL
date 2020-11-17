import sys

sys.stdin = open('bj14890.txt','r')

N,L = map(int,input().split())
hMap = [] #가로
vMap = [[] for _ in range(N)] #세로
for i in range(N) :
    hMap.append(list(map(int,input().split())))
    for j in range(N) :
        vMap[j].append(hMap[i][j])

def check(road, L) :
    i = 0
    visited = [0 for _ in range(N)]

    while i < N -1 :
        # print(i)
        ## 만약 오른쪽 한칸이 나랑 같으면 패스
        if road[i] == road[i+1] :
            i+=1
            continue
        ## 만약 오른쪽칸이 나보다 한칸 높으면 나 포함 왼쪽 L칸체크
        if road[i] + 1 == road[i+1] :
            for j in range(L) :
                if i-j < 0 or road[i-j] != road[i] or visited[i-j] == 1 :
                    return 0
                visited[i-j] = 1
            i+=1
            continue
        ## 만약 오른쪽 칸이 나보다 한칸 낮으면 다음 L칸체크
        if road[i] - 1 == road[i+1] :
            for j in range(1,L+1) :
                if i+j >= N or road[i+j] != road[i+1] or visited[i+j] == 1:
                    return 0
                visited[i+j] = 1
            i+=L
            continue
        return 0
    return 1
res = 0
for i in range(N) :
    res += check(hMap[i], L)
    res += check(vMap[i], L)
print(res)
# check(hMap[4],L)





