def issafe(x,y) :
	return x >= 0 and x < n and y >= 0 and y < n and v[y][x] == 0

def dfs(x,y,temp) :
	global min_v
	if temp >= min_v :
		return
	if x == 0 and y == 0 :
		if temp < min_v :
			min_v = temp
		return
	v[y][x] = 1
	for i in range(4) :
		if issafe(x+dx[i],y+dy[i]) :
			nx = x+dx[i]
			ny = y+dy[i]
			if c[ny][nx] > temp+m[y][x] :
				c[ny][nx] = temp+m[y][x]
				dfs(x+dx[i],y+dy[i],temp+m[y][x])
	v[y][x] = 0
for tc in range(int(input())):
	n = int(input())
	m = []
	min_v = 987654321
	v = [[0]*n for i in range(n)]
	c = [[min_v] * n for i in range(n)]
	for i in range(n) :
		m.append(list(map(int,list(input()))))

	dx = [0,-1,0,1]
	dy = [-1,0,1,0]
	dfs(n-1,n-1,0)
	print("#%d %d"%(tc+1,min_v))