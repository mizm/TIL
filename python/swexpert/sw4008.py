def dfs(d,my_max,my_min,numbers,op) :
    if d >= len(numbers)-1 :
        return 
        
    for idx,i in enumerate(op) :
        if i > 0 :
            op[idx] -= 1
            d+=1
            if i == '+' :
                dfs(d,my_max,my_min,number)

            

for a in range(int(input())) : #총 테스트 케이스의 개수 T
    n = int(input())
    pre_operand = list(map(int,input().split()))
    #example = ['+','-','*','/']
    num = list(map(int,input().split()))
    my_max = -9999
    my_min = 9999
    dfs(d,my_max,my_min,num,op,n)
        
    print(f'#{a+1} {my_max-my_min}')