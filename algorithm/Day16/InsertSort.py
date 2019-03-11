Data = [1,9,3,6,7,0,4,9,5,0]
Data = [69,10,30,2,16,8,31,22]
for i in range(1,len(Data)) :
	key = Data[i]
	for j in range(i-1,-2,-1) :
		if j == -1 :
			break
		if key < Data[j] :
			Data[j+1] = Data[j]
		else :
			break
	Data[j+1] = key
print(Data)