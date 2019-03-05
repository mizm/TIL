def check() :
    re = 1
    for i in range(n):
        Data = input().split()
        if Data[1] in chk :
            if len(Data) != 4 :
                re = 0
    return re
for tc in range(1,11) :
    n = int(input())
    chk = ['*','-','/','+']
    print('#{} {}'.format(tc,check()))
