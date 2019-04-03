# def find(n, k, c):
#     global maxV
#     global minC
#     if (c == 0 or n == k):
#         s = 0
#         # print(card)
#         for i in range(k):
#             s = s * 10 + int(card[i])
#         if (maxV <= s):
#             maxV = s
#             if (minC > c):
#                 minC = c
#     else:
#         lst = list(str(card))
#         for i in range(k):
#             card[n], card[i] = card[i], card[n]
#             cnt = 1 if n != i else 0
#             find(n + 1, k, c - cnt)
#             card[n], card[i] = card[i], card[n]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     c, N = input().split()
#     card = list(c)
#     maxV = 0
#     minC = int(N)
#     for i in range(len(card)):
#         maxV = maxV * 10 + int(card[i])
#     find(0, len(card), int(N))
#     # if (minC % 2 != 0):
#     #     n1 = maxV % 10
#     #     n2 = maxV % 100 // 10
#     #     maxV = maxV // 100 * 100 + n1 * 10 + n2
#     print('#{} {}'.format(tc, maxV))


def dfs(pos,cnt) :
    global max_v,no_c

    if cnt == 0 or pos == k :
        # print(card)
        s = 0
        for i in range(k) :
            s*=10
            s+=card[i]
        if s >= max_v :
            max_v = s
            if no_c > cnt :
                no_c = cnt
        return
    for i in range(k) :
        if i != pos :
            card[pos],card[i] = card[i],card[pos]
            dfs(pos+1,cnt-1)
            card[pos],card[i] = card[i],card[pos]
        else :
            dfs(pos + 1, cnt)
for tc in range(int(input())) :
    m, n = input().split()
    k = len(m)
    max_v = int(m)

    n = int(n)
    no_c = n
    card = list(map(int,m))
    dfs(0,n)
    if no_c > 0 and no_c % 2 == 1:
        temp = max_v%100
        max_v -= temp
        a = temp % 10
        b = temp // 10
        max_v += a *10 +b
    print("#%d %d"%(tc+1,max_v))