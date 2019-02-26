for tc in range(int(input())) :
    n,m = list(map(int,input().split()))
    data = list(map(int,input().split()))
    print(f'#{tc+1} {data[m%n]}')
