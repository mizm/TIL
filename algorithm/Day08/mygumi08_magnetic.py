def check(item) :
    n = len(item)
    pos = 0
    result = 0
    while n > 1 :
        if item[pos] == 2 and pos == 0 :
            item.pop(0)
            n = len(item)
            continue
        if item[n-1] == 1 :
            item.pop()
            n = len(item)
            continue
        if pos >= n-1 :
            break
        if item[pos] == 1 and item[pos+1] == 2 :
            result+=1
        pos += 1
    return result

def solve():
    result = 0
    for i in range(n) :
        if len(data[i]) <= 1 :
            continue
        else :
            result+=check(data[i])
    return result

for tc in range(10) :
    n = int(input())
    data = [[] for i in range(n)]
    for i in range(n) :
        temp = list(map(int, input().split()))
        for j in range(len(temp)) :
            if temp[j] > 0 :
                data[j].append(temp[j])
    print(f'#{tc+1} {solve()}')
# #
# item = [1,1,1,1,1,1,1,2,1,1,2,2,1,1,1,2]
#
# print(check(item))