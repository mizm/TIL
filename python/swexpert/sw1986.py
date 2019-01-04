for i in range(int(input())) :
    k = int(input())
    print(f'#{i+1} {sum([t for t in range(k+1) if t % 2]) - sum([t for t in range(k+1) if not t%2])}')