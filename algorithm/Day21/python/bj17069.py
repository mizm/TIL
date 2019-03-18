def issafe(x,y) :
	return x>=0 and x < n and y >= 0 and y < n and m[y][x] < 1
def dfs(x,y,dir):
	global result
	if x == n-1 and y == n-1 :
		result += 1
		return
	#가로 dir = 0
	if issafe(x+1,y) and dir != 2 :
		dfs(x+1,y,0)
	#세로 dir = 2
	if issafe(x,y+1) and dir != 0 :
		dfs(x,y+1,2)
	#대각선 dir = 1
	if issafe(x+1,y) and issafe(x+1,y+1) and issafe(x,y+1) :
		dfs(x+1,y+1,1)

n = int(input())
m = []
for i in range(n):
	m.append(list
	         (map(int,input().split())))
result = 0
x = 0
y = 0
dfs(1,0,0)
print(result)
