def chkcnt(z) :
    t = z.count('c')
    s = 'roak'
    if z[0] != 'c':
        return False
    for c in s:
        q=z.count(c)
        if t != q :
            return False
    return True
def chkroll(z) :
    c = 'croak'
    to = []
    while True :
        if len(z) < 5 :
            break
        to.clear()
        for i in c :
            if z.find(i) > 0 :
                to.append(z.index(i))
        tmp = 0
        for j in to:
            if tmp <= j :
                tmp = j
            else :
                return False
        for i in c :
            z = z.replace(i,'',1)
    return True
        
for a in range(int(input())):
    s = input()
    if chkcnt(s) and chkroll(s) : 
        r = 0
        c = 'croak'
        cn = 0
        tmp = []
        while True :
            for i in range(len(s)) :
                if c[cn] == s[i] and not i in tmp :
                    tmp.append(i)
                    cn += 1
                    if cn == 5:
                        cn = 0
            r += 1
            if len(tmp) >= len(s) :
                break
            if len(s) < 5 :
                r = -1
                break
    else :
        r=-1
    print(f'#{a+1} {r}')
        
