import sys
sys.stdin = open('병합정렬.txt','r')
def merge_sort(m):
    global cnt
    if len(m) == 1 :
        return m
    #divide
    mid = len(m)// 2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    #conquer
    return merge(left,right)

def merge(left,right) :
    global cnt

    l = len(left)
    r = len(right)
    re = [-1]*(l+r)

    i = j = k = 0
    while i < l and j < r:
        if left[i] < right[j] :
            re[k] = left[i]
            i+=1
            k+=1
        else :
            re[k] = right[j]
            j += 1
            k += 1
    t = k
    while i < l :
        re[k] = left[i]
        chk = 1
        i+=1
        k+=1
    while j < r :
        re[k] = right[j]
        # chk = 1
        j+=1
        k+=1
    if left[l-1] > right[r-1] :
        cnt += 1
    return re

for tc in range(int(input())) :
    n = int(input())
    cnt = 0
    item = list(map(int,input().split()))
    mdata = [0]*n
    item = merge_sort(item)
    # print(item)
    print("#%d %d %d"%(tc+1,item[n//2],cnt))