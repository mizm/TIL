import sys

sys.stdin = open('bj14890.txt', 'r')

N, L = map(int,input().split())

originMap = []
verticalMap = [[] for i in range(N)]
for i in range(N) :
    originMap.append(list(map(int,input().split())))
    for j in range(N) :
        verticalMap[j].append(originMap[i][j])


res = 0
def check(road) :
    global L
    i = 0
    visited = [0 for i in range(N)]
    while i < N - 1:
        # if i == N - 2 :
        #     if road[i] != road[i+1] :
        #         return 0
        chk = True
        #오른쪽 한칸이 나랑 같을 경우 패스
        if road[i+1] == road[i] :
            i+=1
            continue
        #오른쪽이 높을경우 왼쪽에 나랑 같은거 L개 있는지 체크
        if road[i] + 1 == road[i+1] :
            for j in range(L) :
                if i - j < 0 :
                    return 0
                if road[i] != road[i-j] :
                    return 0
                if visited[i-j] == 1 :
                    return 0
            for j in range(L) :
                visited[i-j] = 1
            i+=1
            continue
        #오른쪽이 나보다 낮을 경우 오른쪽으로 L개가 같은지 체크
        if road[i] - 1 == road[i+1] :
            for j in range(L) :
                if i + j + 1 >= N :
                    return 0
                if road[i+1] != road[i+1+j] :
                    return 0
                if visited[i+1+j] == 1 :
                    return 0
            for j in range(L):
                visited[i + 1 + j] = 1
            i+=L
            continue
        if chk :
            return 0
    return 1

for i in range(N) :
    res += check(verticalMap[i][:])
    res += check(originMap[i][:])
print(res)