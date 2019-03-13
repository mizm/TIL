def prime(n) :
	if n < 2 :
		return False
	i = 2
	while i*i <= n :
		if n%i == 0 :
			return False
		i+=1
	return True
for tc in range(int(input())) :
	n = int(input())
	a=b=n//2
	fa=fb=1
	while True :
		if fa :
			for i in range(a,1,-1) :
				if prime(i) :
					a= i
					break
		if fb :
			for i in range(b,n+1) :
				if prime(i) :
					b = i
					break
		if a+b == n :
			break
		elif a+b > n :
			a-=1
			fb = 0
			fa = 1
		elif a+b < n :
			fa = 0
			fb = 1
			b+=1
	print(a,b)
