def babygin():
	cntA = [0] * 10
	cntB = [0] * 10
	for i in range(12):
		if i % 2:
			cntB[w[i]] += 1
			for j in range(1, 9):
				if cntB[j] >= 3:
					return 2
				if cntB[j-1] and cntB[j] and cntB[j+1] :
					return 2
		else :
			cntA[w[i]] += 1
			for j in range(1, 9):
				if cntA[j] >= 3:
					return 1
				if cntA[j-1] and cntA[j] and cntA[j+1] :
					return 1
	return 0
for tc in range(int(input())) :
	w = list(map(int,(input().split())))
	print("#%d %d"%(tc+1,babygin()))
