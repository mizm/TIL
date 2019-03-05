def inorder(r) :
    if r*2 <= n :
        inorder(r*2)
    print(tree[r],end='')
    if r*2+1 <= n :
        inorder(r*2+1)
for tc in range(1,11) :
    n = int(input())
    tree = ['']*(n+1)
    for i in range(n) :
        Data = input().split()
        tree[i+1] = Data[1]
    print('#{}'.format(tc),end='')
    inorder(1)
    print()