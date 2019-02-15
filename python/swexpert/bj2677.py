def dfs(i,j):
    global l
    global k
    l[i][j] = 0
    k += 1
    if i - 1 >= 0 and l[i-1][j] :
        dfs(i-1, j)
    if j + 1 < n and l[i][j+1] :
        dfs(i, j + 1)
    if i + 1 < n and l[i+1][j] :
        dfs(i + 1, j)
    if j-1 >= 0 and l[i][j-1] :
        dfs(i, j - 1)
    return



n =int(input())
l=[]
for i in range(n) :
    l.append(list(map(int,list(input()))))
item = []
for i in range(n) :
    for j in range(n) :
        if l[i][j] == 1 :
            k = 0
            dfs(i,j)
            item.append(k)
print(len(item))
for i in sorted(item) :
    print(i)