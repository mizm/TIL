def mysqrt(n) :
    if n == 1 :
        return 1
    a=b=0
    for i in range(n):
        if (i+1)**2 > n :
            break
    b = i+1
    a = i
    c = 0
    while True :
        if round(a**2,6) == round(b**2,6) :
            return a
        c = (a+b)/2
        if c**2 > n :
            b = c
        else :
            a = c
def mysqrt(n,a,b) :
    if n == 1 :
        return 1
    if a == 0 and b == 0 :
        a=b=0
        for i in range(n):
            if (i+1)**2 > n :
                break
        b = i+1
        a = i
        return mysqrt(n,a,b)

    if round(a**2,6) == round(b**2,6) :
        return a
    c = 0
    c = (a+b)/2
    if c**2 > n :
        b = c
    else :
        a = c
    return mysqrt(n,a,b)
print(mysqrt(5,0,0))

from math import sqrt
print(sqrt(5))
        
print('111000'.count('1'))
    