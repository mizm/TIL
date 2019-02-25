def divide(start,end) :
    if start == end :
        return start
    item1 = divide(start, (start+end)//2)
    item2 = divide((start + end) // 2 + 1,end)
    if data[item2-1] in di[data[item1-1]]:
        return item1
    else:
        return item2

for tc in range(int(input())) :
    di = {1:[1,3], 2:[2,1], 3:[2,3]}
    n = int(input())
    data = list(map(int, input().split()))
    print(f'#{tc+1} {divide(1,n)}')