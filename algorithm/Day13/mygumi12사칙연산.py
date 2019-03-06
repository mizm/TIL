def postorder(r) :
    if left[r] > 0:
        postorder(left[r])
    if right[r] > 0 :
        postorder(right[r])
    if tree[r].isdigit()  :
        stack.append(int(tree[r]))
    print(tree[r],end=' ')
    if len(stack) > 1:
        if tree[r] == '+' :
            item2 = stack.pop()
            item1 = stack.pop()
            stack.append(item1+item2)
        if tree[r] == '-' :
            item2 = stack.pop()
            item1 = stack.pop()
            stack.append(item1-item2)
        if tree[r] == '*' :
            item2 = stack.pop()
            item1 = stack.pop()
            stack.append(item1*item2)
        if tree[r] == '/' :
            item2 = stack.pop()
            item1 = stack.pop()
            stack.append(item1/item2)

for tc in range(1,11) :
    n = int(input())
    left = [0]*(n+1)
    right = [0]*(n+1)
    tree = [0]*(n+1)
    for i in range(n) :
        Data = input().split()
        tree[int(Data[0])] = Data[1]
        if len(Data) >= 3 :
            left[int(Data[0])] = int(Data[2])
        if len(Data) == 4 :
            right[int(Data[0])] = int(Data[3])
    stack = []
    postorder(1)
    print('#{} {}'.format(tc,int(stack[0])))
