item = [1,2,3]
#중복순열
result = [0,0,0]
visited = [0]*3
def dfs(pos) :
	if pos >= 3 :
		print(result)
		return
	for i in range(3) :
		if not visited[i] :
			visited[i] = 1
			result[pos] = item[i]
			dfs(pos+1)
			visited[i] = 0
			result[pos] = -1
dfs(0)

# 순열
result = [0,0]
def dfs(pos) :
	if pos >= 2 :
		if result[0] != result[1] :
			print(result)
		return
	for i in range(pos,3) :
		result[pos] = item[i]
		dfs(pos+1)
		result[pos] = -1
dfs(0)