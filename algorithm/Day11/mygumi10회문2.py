def makePi(pattern) :
    piTable = [0] * len(pattern)
    i = 0
    j = 1
    while j < len(pattern) :
        if pattern[i] != pattern[j] :
            cnt = 0
            if pattern[0] == pattern[j] :
                cnt += 1
                i = 1
            j+=1
            piTable[j] = cnt
            continue
        else :
            i+=1
            j+=1
            piTable[j] = piTable[j-1]+1
    return piTable
for tc in range(10) :
    k = int(input())
    n = 100
    vertical = [[] for i in range(n)]
    m = 0
    for i in range(n) :
        item = input()
        for i in range(n,m,-1) :
            if check(item,i) :
                m = i
                break
        for j in range(n) :
            vertical[j].append(item[j])
    for i in range(n) :
        item = ''.join(vertical[i])
        for i in range(n,m,-1) :
            if check(item,i) :
                m = i
                break
    print('#{} {}'.format(k, m))