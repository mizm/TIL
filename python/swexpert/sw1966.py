for i in range(int(input())):
    input()
    print(f'#{i+1} ',end='')
    [print(t,end=' ')for t in sorted(map(int,input().split()))]
    print()