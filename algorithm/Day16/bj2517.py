n = int(input())
Data = []
result = [[-1]*(n) for i in range(2)]
rank = [-1]*n
idx = [-1]*n
ranking = [n]*n
# ranking[0] = 1
# cnt = 0

for i in range(n) :
	result[0][i] = int(input())
	result[1][i] = i

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
	re = [-1]*(l+r)

	i = j = k = 0
	while i < l and j < r:
		# if not i == j :
		# 	cnt += 1
		if left[i] < right[j] :
			re[k] = right[j]

			j+=1
			k+=1
		else :
			re[k] = right[i]
			i += 1
			k += 1
	t = k
	while i < l :

		# 	print(j, cnt)
		re[k] = left[i]
		i+=1
		k+=1
		# if j == r-1 :
		# 	cnt+=k
	while j < r :
		# cnt += 1
		re[k] = right[j]
		j+=1
		k+=1
	return re
merge_sort(Data)

# print(result)
print(ranking)
print(idx)
