x1,y1,x2,y2 = map(int,input().split())

a = [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]
x1,y1,x2,y2 = map(int,input().split())

b = [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]

x1,y1 = a[0]
x2,y2 = a[3]
x3,y3 = b[0]
x4,y4 = b[3]
def checknull():
    res = 0
    for i in range(4) :
        kx,ky = b[i]
        if x1 <= kx <= x2 and y1 <= ky <= y2 :
            res+=1
        else :
            continue
    if res == 0 :
        print("NULL")
        return True
    else :
        return False
def checkpoint():
    res = 0
    for i in range(4):
        for j in range(4):
            if a[i] == b[j] :

                res +=1
                if res >= 2:
                    return False
    if res == 0 :
        return False
    print("POINT")
    return True
def checkline() :
    #x축
    res = 0
    if y1 == y3 or y1 == y4 :
        res += 1
    if y2 == y3 or y2 == y4 :
        res += 1
    if x1 == x3 or x1 == x4 :
        res += 1
    if x2 == x3 or x3 == x4 :
        res += 1
    if res == 1 :
        print("LINE")
        return True
    return False
if not checknull() :
    if not checkpoint():
        if not checkline() :
            print("FACE")