def timec(l,floor) :
    time = 0
    while True :
for a in range(int(input())):
    n =int(input())
    l=[list(map(int,input().split())) for i in range(n)]
    person = [(x,y) for x in range(n) for y in range(n) if l[x][y]==1]
    floor = [(x,y) for x in range(n) for y in range(n) if l[x][y] > 1]
    t = 2**len(person)
    m = t
    for i in range(t) :
        k = timec(bin(i)[2:],floor)
        if m <= k:
            m = k