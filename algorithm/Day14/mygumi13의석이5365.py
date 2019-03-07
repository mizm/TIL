for tc in range(int(input())) :
    Data = []
    max_len = 0
    for i in range(5):
        Data.append(input())
        if max_len < len(Data[i]) :
            max_len = len(Data[i])
    cnt = 0
    print('#%d '%(tc+1),end='')
    while cnt <= max_len :
        for i in Data :
            if len(i) > cnt :
                print(i[cnt],end='')
        cnt+=1
    print()