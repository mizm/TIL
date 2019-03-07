def dfs(pos) :
    if pos > c :
        return
    if len(Data) == r:
        print(Data)
        return
    Data.append(pos+1)
    dfs(pos+1)
    Data.pop()
    dfs(pos+1)
c = 3
r = 2
Data = []
dfs(0)
