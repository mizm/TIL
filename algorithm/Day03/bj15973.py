class rec :
    def __init__(self,args) :
        self.x1 = args[0]
        self.y1 = args[1]
        self.x2 = args[2]
        self.y2 = args[3]

    def check(self, rec1):
        pass
a = rec(list(map(int,input().split())))
b = rec(list(map(int,input().split())))
