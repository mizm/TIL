n = int(input())
Data = []
for i in range(n) :
    Data.append(list(map(int,(input().split()))))
# print(Data)
res =[0,0,0]

def dnq(x1,y1,x2,y2) :
    temp = Data[y1][x1]
    chk = 1
    # print(x1,y1,x2,y2)
    r = (x2 - x1 + 1) // 3
    for i in range(x1,x2+1) :
        for j in range(y1,y2+1) :
            if temp != Data[j][i] :
                chk = 0
                break
    if chk :
        if temp == -1 :
            res[0] += 1
        elif temp == 0 :
            res[1] += 1
        elif temp == 1:
            res[2] += 1
        return
    else :
        dnq(x1, y1, x1 + r - 1, y1 + r - 1)
        dnq(x1+r, y1, x1 + r + r - 1, y1 + r - 1)
        dnq(x1+r+r, y1, x1+r+r + r - 1, y1 + r - 1)
        dnq(x1, y1+r, x1 + r - 1, y1 +r + r - 1)
        dnq(x1+r, y1+r, x1+r + r - 1, y1 +r + r - 1)
        dnq(x1+r+r, y1+r, x1+r+r + r - 1, y1 +r + r - 1)
        dnq(x1, y1 +r+ r, x1 + r - 1, y1 +r + r + r - 1)
        dnq(x1 + r, y1+r + r, x1 + r + r - 1, y1+r  + r + r - 1)
        dnq(x1 + r + r, y1 +r + r, x1 + r + r + r - 1, y1 +r + r + r - 1)
dnq(0,0,n-1,n-1)
for i in res :
    print(i)