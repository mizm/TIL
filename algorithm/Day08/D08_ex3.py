def backtrack(p) :
    global item
    k = sum(item)
    if k > 10 :
        return
    if k == 10 :
        print(item)
        return
    for i in range(p,10) :
        item.append(i+1)
        backtrack(p+1)
        item.pop()


# data = [1,2,3,4,5,6,7,8,9,10]
item = []
backtrack(0)