# def check_Film():
#     global d,w,k,item,min_result
#     if k == 1 :
#         return 0
#     for i in range(0,2**d) :
#         result = solve(bin(i)[2:].zfill(d))
#         if min_result > result :
#             min_result = result
# # def solve(binstring) :
# #     global item,min_result
# #     cnt = binstring.count('1')
# #     if cnt > min_result :
# #         return 100
# #     checkitem = []
# #     for j in range(0,2**cnt) :
# #         selectchange = bin(j)[2:].zfill(cnt)
# #         selectidx = 0
def check() :
    global item,d,w,k
    for i in range(w) :
        temp = -1
        cnt = 0
        for j in item :
            if temp != j[i] :
                temp = j[i]
                cnt = 1
            else :
                cnt += 1
            if cnt >= k :
                break
        if cnt < k :
            return False
    return True
def dfs(pos,change,cnt) :
    global item,d,w,k,min_result
    if k == 1 :
        min_result = 0
        return
    if pos >= d :
        if check() :
            if min_result > cnt :
                min_result = cnt
        return
    if cnt > min_result :
        return
    if change > -1 :
        cnt+=1
    if change == -1 :
        for i in range(-1,2):
            dfs(pos+1,i,cnt)
    else :
        for i in range(-1,2) :
            temp = item[pos][:]
            item[pos] = [change for j in range(w)]
            dfs(pos+1,i,cnt)
            item[pos] = temp
for a in range(int(input())) :
    d,w,k = list(map(int,input().split()))
    item=[list(map(int,input().split())) for i in range(d)]
    min_result = 100
    for i in range(-1,2):
        dfs(0,i,0)
    print(f'#{a+1} {min_result}')

