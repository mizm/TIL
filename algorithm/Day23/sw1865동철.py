# for tc in range(int(input())) :
# 	n = int(input())
# 	ma = []
# 	for i in range(n) :
# 		ma.append(list(map(int,input().split())))
# 	c = [-1] * n
# 	for i in range(n-2,-1,-1) :

	# res = []
	# while len(res) < n :
	# 	t = 0
	# 	a = -1
	# 	b = -1
	# 	for i in range(n) :
	# 		for j in range(n) :
	# 			if ma[i][j] > t :
	# 				t = ma[i][j]
	# 				a = i
	# 				b = j
	# 	res.append(t)
	# 	for i in range(n) :
	# 		ma[a][i] = -1
	# 		ma[i][b] = -1
	# r = 1
	# for i in res :
	# 	r*=(i/100)
	# print("#%d %0.6f"%(tc+1,round(r*100,6)))



# def dfs(pos) :
# 	global my_max
# 	if pos >= n :
# 		temp = 1
# 		for i in range(n) :
# 			temp *= ma[i][data[i]]/100
# 		if my_max < temp :
# 			my_max = temp
# 		return
# 	for i in range(n) :
# 		if ma[pos][i] > 0 :
# 			if ma[pos][i] <= my_max*100 :
# 				return
# 			if data[i] == -1 :
# 				data[i] = i
# 				dfs(pos+1)
# 				data[i] = -1

def dfs(pos,item) :
	global my_max
	# print(item,my_max)
	if item <= my_max :
		return
	if pos >= n :

		if item > my_max :
			print(data)
			my_max = item
			# print(my_max)
		return
	for i in range(n) :
		if data[i] == 0 :
			data[i] = 1
			dfs(pos+1,item*(ma[i][pos]/100))
			data[i] = 0
for tc in range(int(input())) :
	n = int(input())
	ma = []
	for i in range(n) :
		ma.append(list(map(int,input().split())))
	data = [0]*n
	my_max = 0
	dfs(0,1)
	print("#%d %0.6f" % (tc + 1, round(my_max*100, 6)))