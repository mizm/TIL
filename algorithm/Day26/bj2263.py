def check(s,e,root) :

    # if s > e :
    #     print(check1[s])
    #     return
    # print(root)
    print(check1[root],end=' ')
    left = -1
    for i in range(root,-1,-1) :
        if left > -1 : break
        for j in range(s,root) :
            if check1[j] == check2[i] :
                left = j
                break
    if left > -1 :
        check(s,root,left)
    right = -1
    for i in range(n-1,root-1,-1) :
        if right > -1 : break
        for j in range(root+1,e) :
            if check1[j] == check2[i] :
                right = j
                break
    if right > -1 :
        check(root+1,e,right)

n = int(input())
check1 = list(map(int,input().split()))
check2 = list(map(int,input().split()))
# print(check2[n-1])
for i in range(n) :
    if check1[i] == check2[n-1] :
        r = i
check(0,n,r)