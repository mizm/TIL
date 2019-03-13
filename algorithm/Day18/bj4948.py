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
n=123456*2+1
c = [-1] * n

while n :
	n = int(input())
	if n == 0 :
		break
	cnt = 0
	for i in range(n+1,n*2+1) :
		if prime(i) :
			# print(i)
			cnt += 1
	print(cnt)