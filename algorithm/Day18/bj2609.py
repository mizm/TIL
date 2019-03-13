def gcd(a,b) :
	while b != 0 :
		t = b
		b = a%b
		a = t
	return a
a,b = map(int,input().split())
t = gcd(a,b)
print(t)
print((a*b)//t)