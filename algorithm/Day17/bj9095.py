c = [-1]*(1000001)
c[0] = 0
c[1] = 1
c[2] = 2
c[3] = 4
def dp(n) :
	if c[n] >= 0 :
		return c[n]
	else :
		for i in range(4, n+1):
			c[i] = (c[i - 1] + c[i - 2] + c[i - 3]) %1000000009
		return c[n]
for tc in range(int(input())) :
	n = int(input())
	# c[4] = 7
	# c[5] = 13
	print(dp(n))
# cnt = 0
# def dfs(pos) :
# 	global cnt
# 	if pos >= n :
# 		if pos == n:
# 			cnt += 1
# 		return
# 	dfs(pos+1)
# 	dfs(pos+2)
# 	dfs(pos+3)
#
# n = int(input())
# dfs(0)
# print(cnt)