l=[2,3,5,7,11]
for a in range(int(input())) :
    n=int(input())
    print(f'#{a+1} ',end ='')
    for i in l:
        k=0
        while True:
            if n%i or n <= 1:
                break
            n = n//i
            k+=1
        print(k,end=' ')
    print()