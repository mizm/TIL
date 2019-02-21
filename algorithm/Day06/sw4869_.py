def dp(n):
    if n == 1 :
        return 0
    f = [1, 3]
    for i in range(2,n) :
        f.append(2*f[i-2] + f[i-1])
    return f[n-1]
for tc in range(int(input())) :
    cnt = 0
    n = int(input())
    print(f'#{tc+1} {dp(n//10)}')