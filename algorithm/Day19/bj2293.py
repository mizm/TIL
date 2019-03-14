def knapsack(n,k) :

	for i in range(2,n+1) :
		for j in range(1,k+1) :
			if j > data[i-1] :
				c[i][j] = c[i-1][j]+c[i][j-data[i-1]]
			else :
				t = 0
				if j - data[i - 1] == 0:
					t = 1
				c[i][j] = c[i-1][j]+t
	return(c[n][k])
n,k = map(int,input().split())
data = [int(input()) for i in range(n)]
c = [0]*(k+1)
c[0] = 1
for i in range(n) :
	for j in range(1,k+1) :
		if j >= data[i] :
			c[j] += c[j-data[i]]

print(c[k])
# for i in c :
# 	print(i)

