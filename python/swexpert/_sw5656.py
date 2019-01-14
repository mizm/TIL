def dfs(t,pre_map) :
    global my_max
    global n,w,h
    temp_map = pre_map[:]
    if t >= n :
        result = h*w - temp_map.count(0)
        if result > my_max :
            my_max = result
        return
    temp2_map = []
    for i in range(w) :
        for j in range(h) :
            if temp[i + w*j] > 0 :
                temp2_map = temp_map[:]
                break
        if temp2_map :
            if temp2_map[i+w*j] == 1 :
                temp2_map[i+w*j] = 0
                dfs(t+1,temp2_map)
            else :
                while True :
                    k = temp2_map[i+w*j] - 1
                    
                    
        

                
                
    

for a in range(int(input())) : #총 테스트 케이스의 개수 T
    n,w,h= list(map(int,input().split()))
    fst_map = []
    for i in range(h) :
        fst_map.extend(list(map(int,input().split())))
    my_max = -9999
    dfs(time,fst_map)  