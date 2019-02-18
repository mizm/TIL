import sys

def issafe(x,y,n) :
    return x >= 0 and x < n and y >= 0 and y < n

sys.stdin = open("D03_ex1_input.txt", 'r')



Data = [[0 for x in range(5)] for y in range(5)]

for i in range(5):
    Data[i] = list(map(int,input().split()))
dx = [0,1,0,-1]
dy = [-1,0,1,0]
result = 0
for y in range(5) :
    for x in range(5) :
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if issafe(nx,ny,5) :
                if Data[y][x] > Data[ny][nx] :
                    result += Data[y][x] - Data[ny][nx]
                else :
                    result += Data[ny][nx] - Data[y][x]
print(result)