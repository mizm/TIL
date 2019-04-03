import collections
# def issafe(x,y) :
# 	return 0 <= x < n and 0<= y < n and not visited1[y][x]
def issafe2(x,y) :
	return 0 <= x < n and 0<= y < n
# def dfs(x,y,pos) :
# 	global max_v1, visited1,t
# 	# t += 1
# 	# print(t)
#
# 	if pos >= max_v1 :
# 		return
# 	if x == tx and y == ty :
# 		if pos < max_v1 :
# 			max_v1 = pos
# 		return
# 	visited1[y][x] = 1
# 	for i in range(8):
# 		nx = x + dx[i]
# 		ny = y + dy[i]
# 		if issafe(nx,ny) :
# 			dfs(nx,ny,pos+1)
# 	visited1[y][x] = 0
def bfs(x,y):
	Q = collections.deque([(x,y,0)])
	t = 0
	while Q :
		# print(t)
		# t+=1
		x,y,l = Q.popleft()
		for i in range(8) :
			nx = x + dx[i]
			ny = y + dy[i]
			if issafe2(nx,ny) and visited[ny][nx] > l+1 :
				Q.append((nx,ny,l+1))
				if nx == tx and ny == ty :
					return l+1
for tc in range(int(input())) :
	n = int(input())
	x,y,tx,ty = map(int,input().split())
	max_v = 987654321
	max_v1 = 987654321
	dx = [2,3,3,2,-2,-3,-3,-2]
	dy = [-3,-2,2,3,3,2,-2,-3]
	visited1 = [[0] * n for i in range(n)]
	visited = [[max_v]*n for i in range(n)]
	t=0
	# dfs(x, y, 0)
	# print(max_v1)
	# print('-------------------------')
	print("#%d %d"%(tc+1,bfs(x,y)))