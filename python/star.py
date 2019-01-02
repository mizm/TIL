def star(cnt):
    for i in range(0,cnt-1) :
        print(' ',end = '')

    print('*')
    for i in range(0,cnt-2) :
        print(' ',end = '')
    print('* *')
    for i in range(0,cnt-3) :
        print(' ',end = '')
    print('*****')

star(24)