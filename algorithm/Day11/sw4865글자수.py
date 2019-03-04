for tc in range(int(input())) :
    str1 = input()
    str2 = input()
    my_max = 0
    for i in str1 :
        item = str2.count(i)
        if item > my_max :
            my_max = item
    print('#{0} {1}'.format((tc+1),my_max))