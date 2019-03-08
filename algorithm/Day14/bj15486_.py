N = int(input())
pay = [0] * (N+1)
t = [0] * (N+1)
p = [0] * (N+1)
for i in range(1, N+1):
    _n, _p = map(int, input().split())
    t[i] = _n
    p[i] = _p
maxpay = 0
for i in range(N, 0, -1):
    timetag = t[i]
    if timetag + i == N + 1:
        if p[i] > maxpay:
            pay[i] = p[i]
            maxpay = pay[i]
        else:
            pay[i] = maxpay
    elif timetag + i < N + 1:
        paytag = pay[timetag + i] + p[i]
        if maxpay < paytag:
            pay[i] = paytag
        else:
            pay[i] = maxpay
    else:
        pay[i] = maxpay
    if maxpay < pay[i]:
        maxpay = pay[i]
print(pay)
print(maxpay)