l = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(int(input())) :
    s = input()
    y = s[0:4]
    m = int(s[4:6])
    d = int(s[6:8])
    if m < 1 or m > 12 or d < 1 or d > l[m-1]:
        print(f'#{i+1} -1')
        continue
    else :
        print(f'#{i+1} {y.zfill(4)}/{str(m).zfill(2)}/{str(d).zfill(2)}')
    