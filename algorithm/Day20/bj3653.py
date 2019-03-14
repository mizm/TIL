for tc in range(int(input())) :
	n, m = map(int,input().split())
	tree = [0]*(n+1)
	for i in range(1,n+1) :
		tree[i] = i
	print(tree)
