l=[50000,10000,5000,1000,500,100,50,10]
for i in range(int(input())):
    t=int(input()) 
    print(f'#{i+1}')
    for j in l:
        print(t // j,end=' ')
        t-=j*(t//j)
    print()