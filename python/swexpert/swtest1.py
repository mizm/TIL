for a in range(int(input())):
    n =int(input())
    l=[list(map(int,input().split())) for i in range(n)]
    core = [(x,y) for x in range(n) for y in range(n) if l[x][y]==1]
    fps = {}
    for x,y in core :# 0:위 1오른쪽 2아래 3 왼쪽
        if x > 0 and y > 0:
            # x,y가 0이면 전원에 닿아있기 떄문에 필요없음
            #위는 y--
            t = 0
            for i in range(y-1,0,-1) :
                if l[x][i] > 0 :
                    t += 1
            print(t)

