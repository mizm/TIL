T = int(input())
for test_case in range(1, T + 1) :
	n,m = input().split()
	print("#%d"%test_case, end= ' ')
	for t in m :
		if t <= '9':
			t = ord(t) - ord('0')
		else:
			t = ord(t) - ord('A') + 10
		# print(t)
		print(bin(t)[2:].zfill(4), end = '')
	print()