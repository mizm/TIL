def go() :
    if s == "up" or s == "down" :
        if s== "up" :
            for i in v:
                temp = []
                for j in range(n):
                    item = i.pop(0)
                    if item > 0 :
                        if len(temp) == 0:
                            temp.append(item)
                            flag = False
                        else :
                            if temp[len(temp)-1] == item and not flag:
                                temp[len(temp)-1] *= 2
                                flag = True
                            else :
                                temp.append(item)
                                flag = False
                for j in range(n-len(temp)) :
                    temp.append(0)
                i.extend(temp)
        if s == "down" :
            for i in v:
                temp = []
                for j in range(n):
                    item = i.pop()
                    if item > 0 :
                        if len(temp) == 0:
                            temp.insert(0,item)
                            flag = False
                        else :
                            if temp[0] == item and not flag:
                                temp[0] *= 2
                                flag = True
                            else :
                                temp.insert(0,item)
                                flag = False
                for j in range(n-len(temp)) :
                    temp.insert(0,0)
                i.extend(temp)
        for i in range(n) :
            for j in range(n) :
                print(v[j][i],end=' ')
            print()
    elif s == 'right' or s =='left' :
        if s== "left" :
            for i in h:
                temp = []
                for j in range(n):
                    item = i.pop(0)
                    if item > 0 :
                        if len(temp) == 0:
                            temp.append(item)
                            flag = False
                        else :
                            if temp[len(temp)-1] == item and not flag:
                                temp[len(temp)-1] *= 2
                                flag = True
                            else :
                                temp.append(item)
                                flag = False
                for j in range(n-len(temp)) :
                    temp.append(0)
                i.extend(temp)
        if s == "right" :
            for i in h:
                temp = []
                for j in range(n):
                    item = i.pop()
                    if item > 0 :
                        if len(temp) == 0:
                            temp.insert(0,item)
                            flag = False
                        else :
                            if temp[0] == item and not flag:
                                temp[0] *= 2
                                flag = True
                            else :
                                temp.insert(0,item)
                                flag = False
                for j in range(n-len(temp)) :
                    temp.insert(0,0)
                i.extend(temp)
        for i in range(n):
            print(' '.join(list(map(str,h[i]))))

for tc in range(int(input())) :
    n,s = input().split()
    n = int(n)
    v = [[] for i in range(n)]
    h = []
    for i in range(n) :
        h.append(list(map(int,input().split())))
        for j in range(n):
            v[j].append(h[i][j])
    print('#%d'%(tc+1))
    go()
