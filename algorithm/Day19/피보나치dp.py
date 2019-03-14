n = int(input())
c = [-1]*(n+1)

c[1]=1
c[2]=1
for i in range(3,n+1):
	c[i] = c[i-1]+c[i-2]
print(c[n])