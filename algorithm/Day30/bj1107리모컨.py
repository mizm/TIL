def per(item) :
    if item in m :
        return False
    while item > 0 :
        if item%10 in m :
            return False
        item //= 10
    return True

m_ch = 100
c_ch = input()
n = int(input())
k = int(c_ch)
if n > 0 :
    m = list(map(int,input().split()))
    my_min = 987654321
    min_item = 0
    chk = len(c_ch)
    if chk < abs(k-100) :
        sitem = int(c_ch)
        for i in range(1000001) :
            t = abs(k - i)
            if t < my_min :
                if per(i) :
                    my_min = t
                    min_item = i
    # print(my_min,min_item)
    print(min(len(str(min_item))+my_min,abs(k-100)))
else :
    print(min(len(c_ch), abs(k - 100)))