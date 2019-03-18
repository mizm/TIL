item = input()
n = len(item)
print(item)
for i in range(0,n,7) :
	res = 0
	for j in range(i,i+7):
		if item[j] == '1' :
			res += 1 << i+6-j

	print(res)