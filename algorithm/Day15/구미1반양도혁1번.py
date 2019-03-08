def check() :
    result = 987654321
    if k == 1 :
        return 0
    for i in range(n-k+1) :
        for j in range(n-k+1) :
            #오른쪽밑
            rc=lc=0
            for t in range(k) :
                rc += Data[i+t][j+t]
            for t in range(k) :
                lc += Data[i+t][j+k-1-t]
            temp = abs(rc-lc)
            if temp < result :
                result = temp
    return result



for tc in range(int(input())):
    n,k = map(int,input().split())
    Data = []
    for i in range(n):
        Data.append(list(map(int,input().split())))
    print('#%d %d'%((tc+1),check()))
