for i in range(1,11):
    num_apart=int(input()) #아파트숫자
    high_list=list(map(int,input().split()))#아파트높이
    my_sum = 0
    for j in range(num_apart):
        if high_list[j] > 0 :
            side = [high_list[j-2],high_list[j-1],high_list[j+1],high_list[j+2]]
            m = 255
            for k in side :
                temp = high_list[j] - k
                if temp < 0 :
                    m = 0
                    break
                if temp < m :
                    m = temp
            my_sum+=m
    print(f'#{i} {my_sum}')