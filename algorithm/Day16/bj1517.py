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
			re[k] = left[i]
			cnt += j
			i+=1
			k+=1
		else :
			re[k] = right[j]
			j += 1
			k += 1
	t = k
	while i < l :
		# cnt+=1
		cnt += j
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

n = int(input())
Data = list(map(int,input().split()))
cnt = 0
Data = merge_sort(Data)
print(cnt)