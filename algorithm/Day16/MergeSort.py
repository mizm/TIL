def merge_sort(m):
	if len(m) == 1 :
		return m
	#divide
	mid = len(m)// 2
	left = merge_sort(m[:mid])
	right = merge_sort(m[mid:])
	#conquer
	return merge(left,right)

def merge(left,right) :
	l = len(left)
	r = len(right)
	re = [-1]*(l+r)
	i=j=k=0
	while i < l and j < r:
		if left[i] < right[j] :
			re[k] = left[i]
			i+=1
			k+=1
		else :
			re[k] = right[j]
			j+=1
			k+=1
	while i < l :
		re[k] = left[i]
		i+=1
		k+=1
	while j < r :
		re[k] = right[j]
		j+=1
		k+=1
	print(re)
	return re

Data = [38,27,43,3,9,8,10,1]
n = 7
print(merge_sort(Data))
