item = [1,2,3]
#조합
for i in range(3) :
	for j in range(i+1,3) :
		print(item[i],item[j])
#중복조합
for i in range(3) :
	for j in range(i,3) :
		print(item[i],item[j])
