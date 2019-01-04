for i in range(int(input())):
    k = sorted(map(int,input().split()))[1:-1]
    print(f'#{i+1} {round(sum(k)/len(k))}')