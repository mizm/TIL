for i in range(int(input())) :
    s = input()
    print(f'#{i+1} 1') if s == s[::-1] else print(f'#{i+1} 0')
    