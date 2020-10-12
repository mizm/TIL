import sys

sys.stdin = open('bj17070.txt', 'r')

N = int(input())

originMap = []
visited = []
for i in range(N) :
    originMap.append(list(map(int,input().split())))
    visited.append([[0,0,0] for i in range(N)])
res = 0
# 0 오 1 아래 2 대각
# do dp

visited[0][1][0] = 1
for i in range(0,N) :
    for j in range(1,N) :
        if j < N-1 and originMap[i][j+1] == 0 :
            visited[i][j+1][0] = visited[i][j][0] + visited[i][j][2]
        if i < N-1 and originMap[i+1][j] == 0 :
            visited[i+1][j][1] = visited[i][j][1] + visited[i][j][2]
        if i<N-1 and j < N-1 and  originMap[i+1][j+1] == 0 and originMap[i+1][j] == 0 and  originMap[i][j+1] == 0 :
            visited[i+1][j+1][2] = visited[i][j][0] + visited[i][j][1] + visited[i][j][2]
print(sum(visited[N-1][N-1]))
#
#
# n = int(input())
# p = [[0]*(n+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
# d = [[[0]*3 for _ in range(n+1)] for _ in range(n+1)]
#
# def solve():
#     d[1][2][0] = 1
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if j < n and not p[i][j+1]:
#                 d[i][j+1][0] += d[i][j][0] + d[i][j][2]
#             if i < n and not p[i+1][j]:
#                 d[i+1][j][1] += d[i][j][1] + d[i][j][2]
#             if i < n and j < n and not (p[i+1][j] or p[i][j+1] or p[i+1][j+1]):
#                 d[i+1][j+1][2] += d[i][j][0] + d[i][j][1] + d[i][j][2]
#
# solve()
# for i in range(n+1) :
#     print(d[i])
# print(sum(d[n][n]))

