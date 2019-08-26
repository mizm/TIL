import sys

sys.stdin = open('bj14888.txt','r')

N = int(input())

item = list(map(int,input().split()))
p,m,x,n = map(int,input().split())
maxres = -1000000001
minres = 1000000001
def dfs(pos,r,p,m,x,n) :
    global maxres,minres,N,item
    if p==0 and m==0 and x == 0 and n == 0:
        if r > maxres :
            maxres = r
        if r < minres :
            minres = r
        return
    if p > 0 :
        dfs(pos+1,r+item[pos],p-1,m,x,n)
    if m > 0 :
        dfs(pos+1,r-item[pos],p,m-1,x,n)
    if n > 0 :
            dfs(pos+1,int(r/item[pos]),p,m,x,n-1)
    if x > 0 :
        dfs(pos+1,r*item[pos],p,m,x-1,n)

dfs(1,item[0],p,m,x,n)
print(maxres,minres,sep="\n")