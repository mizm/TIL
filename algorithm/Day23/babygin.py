item = [1,0,1,1,2,3]
def baby() :
	for i in range(6) :
		for j in range(6) :
			if i != j:
				for k in range(6) :
					if j != k and i != k:
						for q in range(6) :
							if k != q and i != q and j != q:
								for r in range(6) :
									if q != r and i != r and j != r and q != r and k != r:
										for t in range(6) :
											if r != t and i != t and j != t and q != t and k != t:
												if item[i] == item[j] == item[k] and item[q] == item[r] == item[t]:
													return 1
												if item[q] == item[r] == item[t] and item[q] + 2 == item[r] + 1 == item[t] :
													return 1
												if item[i] +2 == item[j]+1 == item[k] and item[q] == item[r] == item[t]:
													return 1
												if item[i] +2 == item[j]+1 == item[k] and item[q] + 2 == item[r] + 1 == item[t] :
													return 1
	return 0



print(baby())