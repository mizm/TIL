def power1(a,b) :
    ans = 1
    while b > 0 :
        if b&1 : ans *= a
        a = a*a
        b //= 2
    return ans

print(power1(2,4))