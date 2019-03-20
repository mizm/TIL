#부분집합 합
item = [-1,3,-9,6,7,-6,1,5,4,-2]
temp = []
def dfs(pos) :
	if len(temp) > 0 and sum(temp) == 0 :
		print(temp)
		return
	if pos >= 10 :
		return

	temp.append(item[pos])
	dfs(pos+1)
	temp.pop()
	dfs(pos + 1)
dfs(0)