def pascal(pos) :
    if pos == n+1 :
        return
    if pos == 1 :
        print(1)
        item[0].append(1)
    if pos == 2 :
        print(1,1)
        item[1].append(1)
        item[1].append(1)
    if pos > 2 :
        item[pos-1].append(1)
        for k in range(len(item[pos-2])-1) :
            item[pos-1].append(item[pos-2][k]+item[pos-2][k+1])
        item[pos-1].append(1)
        print(' '.join(list(map(str,item[pos-1]))))
    pascal(pos+1)
for tc in range(int(input())) :
    n = int(input())
    item = [[] for i in range(n)]
    print('#{}'.format(tc+1))
    pascal(1)