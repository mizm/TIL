l = [31,28,31,30,31,30,31,31,30,31,30,31]
for a in range(int(input())) :
    a,b,c,d = list(map(int,input().split()))
    d += sum([l[t] for t in range(a-1,c-1)])
    print(d-b+1)