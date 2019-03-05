
def search() :
    distance = [0]*n
    templist = []
    k = 0
    for i in range(n) :
        if dirlist[i] > 0 :
            templist.append(l-position[i])
        else :
            distance[k] = position[i]
            k+=1
    for t in templist :
        distance[k] = t
        k+=1
    c = 0
    key = []
    while c < q :
        temp = []
        item = min(distance)
        for i in range(n) :
            if item == distance[i] :
                distance[i] = 987654645
                temp.append(idlist[i])
        if len(temp) == 2 :
            for tt in sorted(temp) :
                key.append(tt)
        else :
            key.append(temp[0])
        c = len(key)
    return(key[q-1])

for tc in range(int(input())) :
    n,l,q = map(int,input().split())
    idlist = []
    position = []
    dirlist = []
    for i in range(n) :
        p,a = map(int,input().split())
        idlist.append(a)
        position.append(p)
        dirlist.append(a)
    print(search())