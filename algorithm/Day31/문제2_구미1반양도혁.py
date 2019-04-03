def check():
	max_v = -1
	for temp in res :
		garo= [0]*3
		sero= [0]*4
		garo[1],sero[1],sero[2] = temp
		garo[2] = n-1
		sero[3] = m-1
		garo[0] = 0
		sero[0] = -1
		tdata = [0]*6
		for k in range(3) :
			temp = 0
			for i in range(garo[0],garo[1]+1) :
				for j in range(sero[k]+1,sero[k+1]+1) :
					tdata[k] += item[i][j]
					# print(k,i,j)
		for k in range(3) :
			temp = 0
			# print(garo[1]+1,garo[2]+1)
			for i in range(garo[1]+1,garo[2]+1) :
				for j in range(sero[k]+1,sero[k+1]+1) :
					# print(k + 3, i, j)
					tdata[k+3] += item[i][j]
		#
		for i in range(6) :
			for j in range(i+1,6):
				for k in range(j+1,6) :
					tr = abs(tdata[i]-tdata[j]) + abs(tdata[j]-tdata[k]) + abs(tdata[k]-tdata[i])
					if tr > max_v :
						max_v = tr
	return max_v

for tc in range(int(input())) :
	n,m = map(int, input().split())
	item = []
	for i in range(n) :
		item.append(list(map(int,input().split())))
	res = []#1,4,6
	for i in range(n-1) :
		for j in range(m-1) :
			for k in range(j+1,m-1) :
				res.append((i,j,k))
	# print(item[8][9])
	# print(res)
	print("#%d %d"%(tc+1,check()))

