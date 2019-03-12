n = int(input())
c = list(map(int,input().split()))
c.insert(0,-1)

for j in range(1,n+1) :
	if j % 2 == 0:
		c[j] = min(c[j],c[j//2]*2)
	for i in range(1,j//2) :
		c[j] = min(c[j],c[j-i]+c[i])
	# 	c[j] = max(c[j], c[j - 1] + c[1])
	# else :
	# 	c[j] = max(c[j],c[j-1]+c[1])
print(c[n])