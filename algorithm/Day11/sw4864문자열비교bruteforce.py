for tc in range(int(input())):
    pattern = input()
    Text = input()

    n = len(pattern)
    m = len(Text)
    cnt = 0
    p = 0
    while p < m-n+1 :
        for i in range(n) :
            if pattern[i] != Text[i+p] :
                i-=1
                break
        if i == n-1:
            cnt += 1
            break
        p+=1
    print('#{} {}'.format((tc + 1), cnt))