# for i in range(int(input())) :
# 	n = int(input())
#
c = [-1]*100001
cnt = 0
def dfs(pos,t) :
	global cnt
	if pos >= n :
		if pos == n:
			cnt+=1
		return
	if t != 1 :
		dfs(pos+1,1)
	if t != 2 :
		dfs(pos+2,2)
	if t != 3 :
		dfs(pos+3,3)
def dp(pos,t):
	if pos >= n :
		if pos == n :
			return t
		return -1
	if c[pos] != -1 :
		return c[pos]
	k = -1
	if t != 1 :
		k = min(k,dfs(pos+1,1))
	if t != 2 :
		k = min(k, dfs(pos + 2, 2))
	if t != 3 :
		k = min(k, dfs(pos + 3, 3))
	c[pos] = k
	return k
	# dfs(pos + 1,0)
	# dfs(pos+2,0)
	# dfs(pos+3,0)
for i in range(1,11) :
	cnt = 0
	n = i
	dp(0,0)
	print("%d"%cnt)