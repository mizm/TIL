for tc in range(10) :
    input()
    arr = []
    for i in range(100) :
        arr.append(list(map(int,input().split())))
    my_max = 0
    downcross = 0
    upcross = 0
    for i in range(100) :
        row_sum = 0
        col_sum = 0
        for j in range(100) :
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if i == j :
                downcross += arr[i][j]
            if i + j == 99 :
                upcross += arr[i][j]
            if row_sum > my_max :
                my_max = row_sum
            if col_sum > my_max :
                my_max = col_sum
    if upcross > my_max :
        my_max = upcross
    if downcross > my_max :
        my_max = downcross
    print(f'#{tc + 1} {my_max}')

    # a = []
    # c = [0 for x in range(100)]
    # d = b = 0
    # for i in range(100):
    #     a.append(list(map(int, input().split())))
    #     c.append(sum(a[i]))
    #     for j in range(100):
    #         c[j] += a[i][j]
    #     d += a[i][i]
    #     b += a[i][99-i]
    # c.extend([d,b])
    # print(f'#{tc + 1} {max(c)}')