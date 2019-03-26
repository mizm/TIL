import sys
sys.stdin = open('이진탐색.txt','r')
def binarysearch(item) :
    switch = -1
    l = 0
    r = n-1

    while l <= r :
        m = (l + r) // 2
        if a[m] == item :
            return 1
        elif a[m] < item :
            l = m + 1
            if switch == 1 or switch == -1:
                switch = 0
            else :
                return 0
        elif a[m] > item :
            r = m - 1
            if switch == 0 or switch == -1:
                switch = 1
            else :
                return 0
    return 0
for tc in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a)
    b = list(map(int,input().split()))
    cnt = 0
    for i in b :
        cnt += binarysearch(i)

    print("#%d %d"%(tc+1,cnt))