for tc in range(int(input())) :
	n,m = map(int,(input().split()))
	w = list(map(int,(input().split())))
	t = list(map(int,(input().split())))
	item = 0
	w=sorted(w,reverse=True)
	for i in range(n) :
		k = w[i]
		mi = 99888
		idx = -1
		# print(k,t)
		for j in range(len(t)) :
			if t[j] - k >= 0 and t[j]-k < mi :
				mi = t[j]-k
				idx = j
		if mi == 99888:
			continue
		else :
			# print(k)
			item += k
			t.pop(idx)
	print("#%d %d"%(tc+1,item))
