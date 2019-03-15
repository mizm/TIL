Data = [5,1,-4,2,-1,-5,-2,8,-3,6]
n = 10
RangeSum = [0]*10
idx = [0]*10
RangeSum[0] = Data[0]
idx[0] = 1

for i in range(1,10) :
	if Data[i] > Data[i] + RangeSum[i-1] :
		idx[i] = 1
		RangeSum[i] = Data[i]
	else :
		idx[i] = 0
		RangeSum[i] = Data[i] + RangeSum[i-1]
m = 0
start = -1
for i in range(n) :
	if RangeSum[i] > m :
		m = RangeSum[i]
		start = i
k = 0
for i in range(start,-1,-1) :
	if idx[i] == 0 :
		k+=1
	else :
		break
print(RangeSum[start])
for i in range(start-k,start+1) :
	print(Data[i],end =" ")
