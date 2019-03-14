c = [-1]*42
c[1] = 1

for i in range(2,42) :
	if c[i-1] == i-1 :
		c[i] = 2
	elif i-1 - c[i-1] == 1 :
		c[i] = 1
	else :
		c[i] = c[i-1]+3

print(c)