for i in range(int(input())) :
    a = input()
    for j in range(2,31) :
        if a[0:j] == a[j:j*2] :
            break
    print(f'#{i+1} {j}')