for tc in range(int(input())):
    n =int(input())
    number=list(map(int,input().split()))
    # print(f'#{tc} {max(number)-min(number)}')
    tMax = 1
    tMin = 1000000
    for i in number :
        if tMax < i :
            tMax = i
        if tMin > i :
            tMin = i
    print(f'#{tc} {tMax-tMin}')