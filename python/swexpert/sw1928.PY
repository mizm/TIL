l=[chr(k) for k in range(65,91)]+[chr(k) for k in range(97,123)]+[str(k) for k in range(10)]+['+','/']
for i in range(int(input())):
    s=''
    print(f'#{i+1} ',end='')
    for j in input():
        s+=bin(l.index(j))[2:].zfill(6) 
    for i in [s[j*8:(j+1)*(8)] for j in range(len(s)//8)]:
        print(chr(int(i,2)),end='')
    print()
