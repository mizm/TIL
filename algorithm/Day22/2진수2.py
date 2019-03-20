T = int(input())
for test_case in range(1, T + 1) :
	n = float(input())
	i = -1
	k = []
	while n > 0 :
		if 2**i <= n :
			n -= 2**i
			k.append(1)
		else :
			k.append(0)
		i-=1
		if len(k) >= 13 :
			break
	if len(k) >= 13:
		print("#%d overflow"%test_case)
	else :
		s = ''.join(list(map(str,k)))
		print("#%d %s"%(test_case,s))