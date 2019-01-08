for i in range(1,11):
    n=int(input()) #아파트숫자
    l=list(map(int,input().split()))#아파트높이
    s = 0
    for j in range(n):
        if l[j] > 0 :
            side = l[j-2],l[j-1],l[j+1],l[j+2]
            m = 255
            for k in side :
                temp = l[j] - k
                if temp < 0 :
                    m = 0
                    break
                if temp < m :
                    m = temp
            s+=m
    print(f'#{i} {s}')

