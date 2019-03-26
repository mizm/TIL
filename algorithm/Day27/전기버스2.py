import sys
sys.stdin = open('전기버스.txt','r')
for tc in range(int(input())):
    item = list(map(int,input().split()))

    start = 1
    end = item[0]
    cnt = 0
    while True :
        cango = 0
        if start >= end :
            if start == end :
                cnt-=1
            break
        thisgo = start + item[start]
        if start > 1 :
            cnt+=1
        if thisgo >= end :
            break
        for i in range(start+1,thisgo+1) :
            if i+item[i] > cango :
                cango = i+item[i]
                cani = i
        if cango > thisgo :
            start = cani
        else :
            start = thisgo # cnt+=1


    print("#%d %d"%(tc+1,cnt))