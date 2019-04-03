import time
stime = time.time()
# def pset(pos,r) :
# 	global max_v
# 	if r >= max_v :
# 		return
# 	if len(item) >= n :
# 		if r < max_v :
# 			max_v = r
# 		return
# 	for i in range(n):
# 		if not i in item :
# 			item.append(i)
# 			kk = len(item)
# 			pset(pos+1,r+abs(snack[kk-1][0]-robot[i][0])+abs(snack[kk-1][1]-robot[i][1]))
# 			item.pop()
def dfs(pos,r) :
	global max_v
	if r >= max_v :
		return
	if pos >= n :
		if r < max_v :
			max_v = r
		return
	for i in range(n) :
		if not visited[i] :
			visited[i] = 1
			dfs(pos+1,r+my_map[pos][i])
			visited[i] = 0

for tc in range(int(input())) :
	n = int(input())
	robot = []
	snack = []
	item = list(map(int,input().split()))
	for i in range(n) :
		snack.append((item[i*2],item[i*2+1]))
	item = list(map(int, input().split()))
	for i in range(n):
		robot.append((item[i * 2], item[i * 2 + 1]))
	# print(snack)
	# print(robot)
	# item = []
	# max_v = 0
	# for i in range(n) :
	# 	max_v += abs(snack[i][0]-robot[i][0]) + abs(snack[i][1]-robot[i][1])
	# pset(0,0)
	# print("#%d %d" % (tc + 1, max_v))
	my_map = [[0]*n for i in range(n)]
	visited = [0]*n
	for i in range(n) :
		for j in range(n) :
			my_map[i][j] = abs(snack[i][0]-robot[j][0])+abs(snack[i][1]-robot[j][1])
	# print(my_map)
	max_v = 987654321
	dfs(0,0)

	print("#%d %d"%(tc+1,max_v))
	print(time.time()-stime)

