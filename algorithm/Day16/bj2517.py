n = int(input())
Data = []
result = [[-1]*(2) for i in range(n)]
rank = [-1]*n
idx = [-1]*n
ranking = [n]*n
# ranking[0] = 1
# cnt = 0

for i in range(n) :
	result[i][0] = int(input())
	result[i][1] = i
	ranking[i] = i

# Data = [4,3,2,1,6]

def merge_sort(m):
	global cnt
	if len(m) == 1 :
		return m
	#divide
	mid = len(m)// 2
	left = merge_sort(m[:mid])
	right = merge_sort(m[mid:])

	#conquer
	return merge(left,right)

def merge(left,right) :
	global cnt

	l = len(left)
	r = len(right)
	re = [[-1]*(2) for i in range(l+r)]

	i = j = k = 0
	while i < l and j < r:
		# if not i == j :
		# 	cnt += 1
		if left[i][0] < right[j][0] :
			re[k][0] = left[i][0]
			re[k][1] = left[i][1]
			i+=1
			k+=1
		else :
			re[k][0] = right[j][0]
			re[k][1] = right[j][1]
			ranking[right[j][1]] -= i
			j += 1
			k += 1
	t = k
	while i < l :
		# 	print(j, cnt)
		re[k][0] = left[i][0]
		re[k][1] = left[i][1]
		# ranking[left[i][1]] -= j
		i+=1
		k+=1
		# if j == r-1 :
		# 	cnt+=k
	while j < r :
		# cnt += 1
		re[k][0] = right[j][0]
		re[k][1] = right[j][1]
		ranking[right[j][1]] -= i
		j+=1
		k+=1
	return re
result = merge_sort(result)

# print(result)
for i in ranking :
	print(i+1)
# print(right)
