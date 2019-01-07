for i in range(int(input())):
    a,b,c,d=list(map(int,input().split()))
    a+=c
    b+=d
    if b > 59:
        b-=60
        a+=1
    if a>12:
        a-=12
    print(f'#{i+1} {a} {b}')
        