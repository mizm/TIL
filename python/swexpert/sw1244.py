def check(pos,k, c) :
    global my_max, m
    if c == 0 or pos == k :
        temp = 0
        for i in range(k) :
            temp = 10 * temp + item[k]
        if my_max <= temp :
            my_max = temp
            if m > c :
                m = c
    else :
        for i in range(k) :
            item[pos], item[i] = item[i],item[pos]
            cnt = 1 if pos !=i else 0
            check(pos+1,k,c-cnt)
            item[pos], item[i] = item[i], item[pos]

for tc in range(int(input())):
    n, m = list(map(int, input().split()))
    item = []

    while True :
        if n >= 10 :
            item.insert(0,n%10)
            n //= 10
        else :
            item.insert(0,n%10)
            break
    l_item = len(item)
    my_max = 0
    for i in range(l_item) :
        my_max = my_max * 10 + item[i]
    check(0,l_item,m)
    if m%2 :
        n1 = my_max % 10
        n2 = my_max % 100 // 10
        my_max = my_max - n1 - n2*10 + n1*10 + n2


    print(f'#{tc+1} {my_max}')