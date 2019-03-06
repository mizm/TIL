def check(item) :
    if item < 10 :
        return True
    temp = 0
    while item > 0 :
        temp = item%10
        item //= 10
        if item%10 > temp :
            return False
    return True

for tc in range(int(input())) : 
    n = int(input())
    Data = list(map(int,input().split()))
    result = -1
    for i in range(n-1,-1,-1) :
        for j in range(i-1,-1,-1) :
            if result < Data[i]*Data[j] :
                if check(Data[i]*Data[j]) :
                    result = Data[i]*Data[j]
    print('#{} {}'.format((tc+1),result))