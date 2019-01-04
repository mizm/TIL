q=['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']
for i in range(int(input())):
    p=[]
    n,k=map(int,input().split())
    t = 0
    for j in range(n):
        a,b,c=map(int,input().split())
        t1 =0.35*a+0.45*b+0.2*c
        p.append(t1)
        if j == k-1:
            t=t1
    p = sorted(p)
    print(f'#{i+1} {q[p.index(t)//(n//10)]}')
