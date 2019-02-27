s= "reverse this strings"
rs = ""
for i in range(len(s)-1,-1,-1) :
    rs +=s[i]
print(rs)

# itoa

# 123 = "123"
def itoa(num) :
    s = ""
    while num > 0 :
        s = chr(num%10+48) + s
        num//=10
    return s
print(itoa(123))
# atoi

def atoi(s) :
    t = 0
    for i in s :
        i = ord(i)-48
        if i > 9 :
            i -=7
        t *= 16
        t += i
    return t
print(atoi("42FB"))