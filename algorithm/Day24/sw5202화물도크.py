for tc in range(int(input())) :
	n = int(input())
	data = []
	for i in range(n) :
		data.append(list(map(int,input().split())))
	data = sorted(data)
	res = 0
	end = 0
	# print(data)
	for i in range(n) :
		s = data[i][0]
		if end <= s :
			end = data[i][1]
			for j in range(i+1,n) :
				if end > data[j][1] :
					end = data[j][1]
			res += 1

	print("#%d %d"%(tc+1,res))