import sys
sys.stdin = open("bj17136.txt", 'r')

import copy
N,M,D = map(int,input().split())

my_map = [list(map(int,input().split())) for i in range(N)]

max_kill = 0
def dis(shooter, shooted) :
    return abs(shooter[0]-shooted[0]) + abs(shooter[1] - shooted[1])
def shot(idx, t_map) :
    global D
    c = (idx,N)
    m_d = D
    shoot_list = []
    for i in range(N) :
        for j in range(M) :
            if t_map[i][j] == 1 :
                di = dis(c,(j,i))
                if di == 0 :
                    continue
                if di <= D :
                    shoot_list.append((j,i,di))
                    if m_d > di :
                        m_d = di
    if len(shoot_list) == 0 :
        return (M,N,D+1)
    shooted = (M,N,m_d)
    for x,y,d in shoot_list :
        if m_d == d :
            if x < shooted[0] :
                shooted = (x,y,d)
    #print(shoot_list, shooted,m_d)
    return shooted
def go(t_map) :
    re = [ [0 for j in range(M)] for i in range(N)]
    for i in range(N-1) :
        for j in range(M) :
            re[i+1][j] = t_map[i][j]
    return re
def step(shooters, t_map) :
    global max_kill, D
    tmp_kill = 0
    for cnt in range(N+1) :
        # print(t_map)
        shooted_list = []
        for i  in shooters :
            shooted_list.append(shot(i,t_map))
        # print(shooted_list)
        for x,y,d in shooted_list :
            if d > D :
                continue
            if t_map[y][x] == 1 :
                #print(x,y)
                t_map[y][x] = 0
                tmp_kill += 1
        t_map.insert(0,[0 for i in range(M)])
        t_map.pop()
    if tmp_kill > max_kill :
        max_kill = tmp_kill



for i in range(M) :
    for j in range(i+1,M) :
        for k in range(j+1,M) :
            t_m = copy.deepcopy(my_map)
            step((i,j,k),t_m)

# t_m = copy.deepcopy(my_map)
# step((0,1,2),t_m)
print(max_kill)


