for a in range(int(input())) :
    n=int(input())
    t=''
    print(f'#{a+1}')
    for i in range(n):
        b,c=input().split()
        c = int(c)
        t+=b*c
    for j in range(len(t)):
        if not j%10 and j>0:
            print()
        print(t[j],end='')
    print()
        

        
