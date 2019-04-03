# def dfs(pos,left,right) :
#     global res
#
#     if left < right :
#         return
#     if pos == n :
#         res+=1
#         return
#     if su - left < left :
#         print(res)
#         k = n-pos
#         res += (1 << k) * f[k]
#         return
#     for i in range(n) :
#         if not used[i] :
#             used[i] = 1
#             dfs(pos+1,left+m[i],right)
#             dfs(pos+1,left,right+m[i])
#             used[i] = 0

def dfs(pos, left, right,ld,rd):
    if left < right:
        return 0
    if pos == n:
        return 1
    if c[ld][rd] != -1 :
        return c[ld][rd]
    if su - left < left:
        k = n - pos
        return (1 << k) * f[k]
    p = 0
    for i in range(n):
        if not used[i]:
            used[i] = 1
            p += dfs(pos + 1, left + m[i], right,ld+(1<<i),rd)
            p += dfs(pos + 1, left, right + m[i],ld,rd+(1<<i))
            used[i] = 0
    c[ld][rd] = p
    return p
f = [1]*(10+1)
for i in range(1,10+1) :
    f[i] = i*f[i-1]
for tc in range(int(input())) :
    n = int(input())
    m = list(map(int,input().split()))
    res = 0
    used = [0]*n
    su = sum(m)
    c = [[-1]*(1<<(n+1)) for i in range(1<<(n+1))]
    # dfs(0,0,0)
    # for i in range(n) :
    #     used[i] = 1
    #     dfs(1,m[i],0)
    #     used[i] = 0

    print("#%d %d"%(tc+1,dfs(0,0,0,0,0)))
    # for i in c:
    #     print(i)