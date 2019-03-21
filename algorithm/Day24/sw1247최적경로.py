def dfs(pos) :
	global min_value

	if pos >= n :
		dis = 0
		x,y = end
		ex,ey = start
		for i in range(n) :
			x1,y1 = xy_list[path[i]]
			dis += abs(x1-x) + abs(y1-y)
			x = x1
			y = y1
		dis += abs(x1-ex) + abs(y1-ey)
		if dis < min_value :
			min_value = dis
		return

	for i in range(n) :
		if not visited[i] :
			visited[i] = 1
			path[pos] = i
			dfs(pos+1)
			visited[i] = 0

# 3,0,4,1,2
for tc in range(int(input())) :
	n = int(input())
	item = list(map(int,input().split()))
	visited = [0] * n
	min_value = 987654321
	start = (item[0],item[1])
	end = (item[2],item[3])
	xy_list = []
	path = [0]*n
	for i in range(n):
		x = item[(i*2)+4]
		y = item[(i*2)+5]
		xy_list.append((x,y))
	# print(xy_list)
	dfs(0)
	print("#%d %d"%(tc+1,min_value))
