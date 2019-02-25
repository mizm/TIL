def backtrack(k) :
    global my_min
    if sum(visit) > my_min :
        return
    if k >= n :
        temp = sum(visit)
        if temp < my_min :
            my_min = temp
        return
    for i in range(n) :
        if not visit[i] :
            visit[i] = data[k][i]
            backtrack(k+1)
            visit[i] = 0
for tc in range(int(input())) :
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]
    my_min = 9*n
    visit = [0] * n
    backtrack(0)
    print(f'#{tc+1} {my_min}')