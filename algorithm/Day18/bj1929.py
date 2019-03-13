c = [-1]*1000001
def prime(n) :
	if n < 2 :
		return False
	if c[n] != -1 :
		return c[n]
	i = 2
	while i*i <= n :
		if n%i == 0 :
			c[n] = 0
			return False
		i+=1
	c[n] = 1
	return True

m,n = map(int,input().split())
for i in range(m,n+1) :
	if prime(i) :
		print(i)


