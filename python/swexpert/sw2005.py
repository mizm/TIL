for t in range(int(input())):
    print(f'#{t+1}')
    l = []
    temp = []
    for i in range(1,int(input())+1) :
        if i == 1 :
            l = [1]
        elif i == 2 :
            l = [1,1]
        else :
            t = len(l)
            temp.clear()
            temp.append(1)
            for j in range(t):
                if j < t-1 :
                    temp.append(l[j]+l[j+1])
            temp.append(1)
            l.clear()
            l = temp[:]
        for k in l :
            print(k, end=' ')
        print()