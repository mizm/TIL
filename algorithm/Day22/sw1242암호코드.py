def res(ck) :
	# codeRate = [[1, 2, 4, 7], [1, 3, 5, 7], [2, 4, 5, 7], [1, 2, 6, 7], [2, 5, 6, 7], [1, 4, 6, 7], [4, 5, 6, 7],
	#             [2, 3, 6, 7], [3, 4, 6, 7], [2, 3, 4, 7]]
	# code = []
	# x = len(ck)//56
	# n = x * 7
	# if n < 7 :
	# 	return 0
	# print(x,n)
	# # make Code
	# for kk in range(10):
	# 	t = 0
	# 	for i in range(n):
	# 		for j in range(4):
	# 			if i + 1 <= codeRate[kk][j] * x:
	# 				break
	#
	# 		if (j) % 2 == 0:
	# 			t += 1 << i
	# 	code.append(t)
	# # 	endmake
	# print(code)
	print(len(ck))
	tk = [0,0,0,0]
	t_res = []
	i = len(ck) - 1
	while i > -1:
		if ck[i] == '0':
			i -= 1
		else:
			break
	end = i
	flag = 3
	for i in range(end,-1,-1) :
		if flag%2 == 1 and ck[i] == '1' :
			tk[flag] += 1
		elif flag%2 == 1 and ck[i] == '0' :
			flag -= 1
			tk[flag] += 1
		elif flag%2 == 0 and ck[i] == '0' :
			tk[flag] += 1
		elif flag%2 == 0 and ck[i] == '1' :
			flag -= 1
			if flag == -1 :
				break
			tk[flag] += 1
	x = min(tk)

for tc in range(int(input())) :
	n,m = map(int,input().split())
	chk = []
	sec = [[] for i in range(n)]
	for i in range(n) :
		t = input()
		flag = 0
		for j in range(m):
			if t[j] != '0' :
				flag = 1
			sec[i].extend(bin(int(t[j], 16))[2:].zfill(4))
		if flag :
			res(sec[i])
	# for s in sec :
	# 	print(s)
	print("#%d %d" % ((tc + 1), m))
