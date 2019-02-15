for tc in range(1,11):
    n=int(input())
    my_map=list(map(int,input().split()))
    result = 0
    for j in range(n):
        temp_max = max(my_map)
        temp_min = min(my_map)
        if temp_max == temp_min :
            break
        for i in range(100) :
            if my_map[i] == temp_min:
                my_map[i] += 1
                break
        for i in range(100) :
            if my_map[i] == temp_max:
                my_map[i] -= 1
                break
        # my_map[my_map.index(temp_max)] -= 1
        # my_map[my_map.index(temp_min)] += 1
        
    result = max(my_map)-min(my_map)
    print(f'#{tc} {result}')

