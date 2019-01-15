def search(boxi,boxj,x,y):
    global l
    li = l[y][x]
    for i in range(1,boxi):
    
    for j in range(1,boxj):


for a in range(int(input())) :
    n=int(input())
    l=[list(map(int,input().split())) for i in range(n)]
    my_max = -9999
    for x in range(1,n) :
        for y in range(n-2):
            for i in range(2,n) :
                for j in range(2,n) :
                    item = search(i,j,x,y)
                    if item > my_max :
                        my_max = item
    print(my_max)

