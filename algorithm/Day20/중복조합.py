# Data = [1,2,3,4,5]
#
# n = 5
# c = 3
# visited = [[0]*c for i in range(c)]
# def poo(n,c) :
#
#
# nn = 5
# rr = 3
# IsUsed= [0]*(rr+1)
# def GetSome(n , r):
#     if r > rr :
#         for i in range(1, rr+1):
#               print(IsUsed[i], end=' ')
#         print()
#         return
#     if n > nn : return
#     IsUsed[r] = n
#     GetSome(n, r)
#     GetSome(n+1, r+1)
#
#
#
# GetSome(1,1)
#
#

# def dfs(pos) :
#     if pos > c :
#         return
#     if len(Data) == r:
#         print(Data)
#         return
#     Data.append(pos+1)
#     dfs(pos+1)
#     Data.pop()
#     dfs(pos+1)
# c = 5
# r = 3
# Data = []
# dfs(0)

print('---')
cnt = 0
def dfs(pos) :
    global cnt
    if pos > c :
        return
    if len(Data) == r:
        print(Data)
        cnt+=1
        return
    Data.append(pos)
    dfs(pos)
    Data.pop()
    dfs(pos+1)
c = 3
r = 2
Data = []
dfs(1)

print(cnt)

