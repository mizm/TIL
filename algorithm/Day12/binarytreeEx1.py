
v = int(input())
Data = list(map(int,input().split()))

tree = [0] * (100)
tree[1] = 1
v += 1
left = [0]*v
right = [0]*v
child = [0]*v
parent = [0]*v
level = [0]*v



def preorder(r):
    print(r)
    if left[r] > 0 :
        preorder(left[r])
    if right[r] > 0 :
        preorder(right[r])
def inorder(r) :
    if left[r] > 0 :
        inorder(left[r])
    print(r)
    if right[r] > 0 :
        inorder(right[r])
def postorder(r) :
    if left[r] > 0:
        postorder(left[r])
    if right[r] > 0 :
        postorder(right[r])
    print(r)



for i in range(0,len(Data),2) :
    if left[Data[i]] > 0 :
        right[Data[i]] = Data[i+1]
    else :
        left[Data[i]] = Data[i+1]
    child[Data[i]] += 1
    parent[Data[i+1]] = Data[i]
    level[Data[i+1]] = level[Data[i]] + 1
print(left)
print(right)
print(child)
print(parent)
print(level)
preorder(1)
print()
inorder(1)
print()
postorder(1)
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
