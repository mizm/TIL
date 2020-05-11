import sys
sys.stdin = open("bj17136.txt", 'r')

my_map = [list(map(int,input().split())) for i in range(10)]
total = 0
for m in my_map :
    total += sum(m)
paper = [5,5,5,5,5]
def check(x,y) :
    return x >= 0 and x < 10 and y >= 0 and y < 10 and my_map[y][x] == 1
def check_draw(x,y,n) :
    for i in range(y, y+n) :
        for j in range(x, x+n) :
            if not check(j,i) :
                return False
    return True
def draw(x,y,n,p) :
    for i in range(y, y+n) :
        for j in range(x, x+n) :
            my_map[i][j] = p
res = 25
def dfs(x,y, total, p) :
    global res
    if total == 0 :
        if res > p :
            res = p
        return
    if p > res :
        return
    for i in range(10) :
        for j in range(10) :
            if my_map[i][j] == 0 :
                continue
            else :
                for k in range(4,-1,-1) :
                    if paper[k] > 0 :
                        if check_draw(j,i,k+1) :
                            paper[k] -= 1
                            p += 1
                            total -= (k+1) * (k+1)
                            draw(j,i,k+1,0)
                            dfs(x,y,total,p)
                            draw(j,i,k+1,1)
                            paper[k] += 1
                            p -= 1
                            total += (k+1) * (k+1)
                return
if total == 0 :
    print(0)
else :
    dfs(0,0,total,0)
    if res == 25 :
        print(-1)
    else :
        print(res)