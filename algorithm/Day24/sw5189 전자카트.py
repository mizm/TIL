def dfs(pos) :
	global min_item
	if pos >= n-1 :
		k = 0
		s = 0
		for i in path :
			k+= item[s][i+1]
			s=i+1
		k+= item[s][0]
		if k < min_item :
			min_item = k
		return
	for i in range(n-1) :
		if not visited[i] :
			visited[i] = 1
			path[pos] = i
			dfs(pos+1)
			visited[i] = 0

for tc in range(int(input())) :
	n = int(input())
	item = []
	visited=[0]*(n-1)
	path=[-1]*(n-1)
	min_item = 987654321
	for i in range(n) :
		item.append(list(map(int,input().split())))
	dfs(0)
	print("#%d %d"%(tc+1,min_item))