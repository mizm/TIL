for i in range(int(input())) :
    t = list(map(int,input().split()))
    c = '>'if t[0] > t[1] else '<'
    if(t[0] == t[1]) : c = '='
    print(f'#{i+1} {c}')