def inQueue(item,level):
    priQue.append((item,level))
    n = len(priQue)
    if n == 1 :
        return
    n-=1
    while n > 1 :
        if priQue[n][1] > priQue[n//2][1] :
            # print(priQue[n],priQue[n//2])
            priQue[n],priQue[n//2] = priQue[n//2],priQue[n]
            # print(priQue[n], priQue[n // 2])
        n//=2
priQue = [(-1,-1)]
print(priQue)
inQueue(1,1)
print(priQue)
inQueue(0,2)
print(priQue)
inQueue(3,3)
print(priQue)
inQueue(4,3)
inQueue(5,3)
inQueue(6,3)
inQueue(7,3)
inQueue(8,3)
print(priQue)