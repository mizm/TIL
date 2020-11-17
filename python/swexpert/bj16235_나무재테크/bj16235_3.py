import sys
sys.stdin = open('bj16235.txt','r')

class land :
    cnt = 0

    def __init__(self):
        self.energy = 5
        self.trees = []
        self.dies = 0
        self.dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    def __str__(self):
        return f''

    def makeTree(self,age):
        self.trees.append(age)
        land.cnt +=1
    def spring(self) :
        lives = []
        dies = 0
        self.trees.sort()
        for tree in self.trees :
            if tree <= self.energy :
                self.energy -= tree
                lives.append(tree+1)
            else :
                dies += tree
                land.cnt -= 1
        self.trees = lives
        self.energy += int(dies/2)

    # def summer(self):
    #     if self.dies > 0 :
    #         self.energy += int(self.dies / 2)
    #     self.dies = 0

    def fall(self,myMap,x,y,n) :
        for tree in self.trees :
            if tree % 5 == 0 :
                for dx,dy in self.dir :
                    if 0 <= x + dx < n and 0 <= y + dy < n :
                        myMap[y+dy][x+dx].makeTree(1)
    def winter(self, energy):
        self.energy += energy

N,M,K = map(int,input().split())
s2d2 = []
for i in range(N) :
    s2d2.append(list(map(int,input().split())))
myMap = [[land() for _ in range(N)] for __ in range(N)]

for i in range(M) :
    r,c,z = map(int,input().split())
    myMap[r-1][c-1].makeTree(z)

for year in range(K) :
    # 봄
    for i in range(N) :
        for j in range(N) :
            myMap[i][j].spring()
    # # 여름
    # for i in range(N) :
    #     for j in range(N) :
    #         myMap[i][j].summer()
    # 가을
    for i in range(N) :
        for j in range(N) :
            myMap[i][j].fall(myMap,j,i,N)
    # 겨울
    for i in range(N) :
        for j in range(N) :
            myMap[i][j].winter(s2d2[i][j])


print(land.cnt)