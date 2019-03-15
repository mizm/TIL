# cnt = 1
# for x in range(1,101) :
# 	for y in range(x,101) :
# 		for z in range(y,101) :
# 			if x + y + z == 100 :
# 				print(x,y,z,cnt)
# 				cnt += 1

cnt = 0
visited = [[[0]*101 for i in range(101)] for i in range(101)]
def dfs(x,y,z) :
	global cnt
	if x+y+z > 100 :
		return
	if x > y or y > z :
		return
	if x+y+z == 100 :
		cnt += 1
		print(x, y, z)

		return
	if not visited[x+1][y][z] :
		visited[x+1][y][z] = 1
		dfs(x+1,y,z)
	if not visited[x][y+1][z] :
		visited[x][y+1][z] = 1
		dfs(x,y+1,z)
	if not visited[x][y][z+1] :
		visited[x][y][z+1] = 1
		dfs(x,y,z+1)

dfs(1,1,1)
print(cnt)