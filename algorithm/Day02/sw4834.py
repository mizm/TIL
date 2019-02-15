for tc in range(int(input())):
    n =int(input())
    item = int(input())
    count = [0]*10
    for i in range(n) :
        count[item%10] += 1
        item //= 10
    max_num = 0
    max_item = -1
    for i in range(10) :
        if max_num <= count[i] :
            max_num = count[i]
            max_item = i
    print(f'#{tc+1} {max_item} {max_num}')
