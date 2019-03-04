def check(item) :
    if n == m :
        if item == item[::-1] :
            return item
        else :
            return False
    for i in range(n-m+1) :
        temp = item[i:i+m]
        if temp == temp[::-1] :
            return temp
    return False
for tc in range(int(input())) :
    n,m = map(int, input().split())
    vertical = [[] for i in range(n)]
    for i in range(n) :
        item = input()
        c = check(item)
        if c :
            print('#{0} {1}'.format((tc+1),c))
            continue
        for j in range(n) :
            vertical[j].append(item[j])
    for i in range(n) :
        item = ''.join(vertical[i])
        c = check(item)
        if c :
            print('#{0} {1}'.format((tc+1),c))
            continue
