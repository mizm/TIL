# 1,5,10
# 20원까지 최소 동전의 갯수

c = [[-1]*21 for i in range(4)]

for i in range(21) :
	for j in range(4) :
		if i == 0 or j == 0 :
			c[j][i] = 0
		#min