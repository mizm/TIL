def gcd(p,q) :
    if p == q : return p
    if p<q : return gcd(q,p)
    elif q == 0 : return p
    else : return gcd(q, p % q)

for tc in range(int(input())) :
    r,n,k1 = map(int,input().split())
    data = [[] for i in range(n)]
    item = []
    for i in range(n) :
        item.append(list(map(int,input().split())))
    for i in range(n) :
        x, y = item[i]
        for j in range(n) :
            if i != j :
                x1,y1 = item[j]
                a = x1 - x
                b = y1 - y
                k = 1
                if a == 0 :
                    k = 0
                    t1 = 0
                else :
                    t1 = 1 if a > 0 else -1
                if b == 0 :
                    k = 0
                    t2 = 0
                else :
                    t2 = 1 if b > 0 else -1
                if k :
                    k = a/b
                if not (k,t1,t2) in data[i] :
                    data[i].append((k,t1,t2))
    cnt = 0
    A=[0]*(2*n+1)
    # print(data)
    for i in range(n):
        p = len(data[i])
        cnt += p
        A[i+1] = p
    # print(A)
    c = [0] * (n+1)
    b = [0] * (2 * n+1)
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            A[j] = ((A[j]*k1+j)%n) + 1
            A[n+j] = ((A[j]*j+k1)%n)+1
        A.sort()
        b[0] = 1
        for j in range(1,2*n+1) :
            b[j] = ((b[j-1]*A[j]+j) % n) + 1
        c[i] = b[2*n]
    # print(A,c)
    print("#%d %d %d"%(tc+1,cnt,sum(c)))