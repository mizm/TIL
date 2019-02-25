def check(pos) :
    global my_min, temp
    if my_min < temp :
        return
    if pos >= n+1 :
        m = len(visited)
        x2, y2 = visited[m - 1]
        x1, y1 = xy_data[n+1]
        temp += (abs(x2 - x1) + abs(y2 - y1))
        if temp < my_min :
            my_min = temp
        temp -= (abs(x2 - x1) + abs(y2 - y1))
        return
    for i in range(1,n+1) :
        if not xy_data[i] in visited :
            visited.append(xy_data[i])
            m = len(visited)
            x1,y1 = visited[m-1]
            x2,y2 = visited[m-2]
            plus = (abs(x2-x1)+abs(y2-y1))
            temp += plus
            check(pos+1)
            temp -= plus
            visited.pop()
for tc in range(int(input())) :
    n = int(input())
    data = list(map(int, input().split()))
    xy_data = []
    xy_data.append((data[0], data[1]))
    for i in range(4,4+2*n,2) :
        xy_data.append((data[i],data[i+1]))
    xy_data.append((data[2], data[3]))
    visited = [(data[0], data[1])]
    my_min = 100**2
    temp = 0
    check(1)
    print(f'#{tc+1} {my_min}')