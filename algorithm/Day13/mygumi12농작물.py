for tc in range(int(input())) :
    n = int(input())
    p = [input() for i in range(n)]
    x = y = n//2
    r = 0
    for i in range(n):
        for j in range(n) :
            if abs(x - i) + abs(y - j) <= n//2 :
                r+=int(p[i][j])
    print('#{} {}'.format((tc+1),r))