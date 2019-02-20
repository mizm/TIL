n = 5
pos = 0
result = 0
def stairs(n,pos) :
    global result
    if pos == n :
        result+=1
        return
    if pos > n :
        return

    stairs(n,pos+1)
    stairs(n,pos+2)

stairs(10,0)
print(result)

def stairs2(n) :
    f = [0, 1]
    for i in range(2,n+2) :
        f.append(f[i-1]+f[i-2])

    return f[n+1]

print(stairs2(10))