n = int(input())
c = [-1] * (n+3)
c[0] = 0
c[1] = 1
c[2] = 2
# print(item)
for i in range(3,n+1) :
	if c[i] == -1 :
		c[i] = c[i-1] + c[i-2]
print(c[n])