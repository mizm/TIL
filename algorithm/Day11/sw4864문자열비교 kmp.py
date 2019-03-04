def makePi(pattern) :
    piTable = [0] * len(pattern)
    piTable[0] = -1
    i = cnt = 0
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
for tc in range(int(input())):
    pattern = input()
    Text = input()

    piTable = makePi(pattern)
    i = 0
    n = len(pattern)
    m = len(Text)
    cnt = 0
    while True :
        k = 0
        for j in range(i,len(pattern)+i) :
            if pattern[j-i] == Text[j] :
                k += 1
            else :
                break
        if k == n :
           cnt +=1
           break
        else :
            i += k - piTable[k]
            if i > m-n+1 :
                break