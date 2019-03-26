import collections

def check(istart,iend,pstart,pend) :
    stack = collections.deque([[istart,iend,pstart,pend]])

    if istart > iend or pstart > pend:
        return
    while stack :
        ist,ied,pst,ped = stack.pop()
        root = check2[ped]
        print(root, end=' ')
        pos = item[root]
        left = pos-ist
        if pos+1 <= ied and pst+left <= ped-1 :
            stack.append([pos+1, ied,pst+left,ped-1])
        if ist <= pos-1 and pst <= pst+left-1 :
            stack.append([ist,pos-1,pst,pst+left-1])


n = int(input())
check1 = list(map(int,input().split()))
check2 = list(map(int,input().split()))
# print(check2[n-1])

item = [0]*100001
for i in range(n) :
    item[check1[i]] = i
check(0,n-1,0,n-1)

# def check(istart,iend,pstart,pend) :
#     if istart > iend or pstart > pend:
#         return
#
#     root = check2[pend]
#     print(root, end=' ')
#     pos = 0
#     for i in range(istart,iend+1) :
#         if root == check1[i] :
#             pos = i
#             break
#     left = pos-istart
#     check(istart,pos-1,pstart,pstart+left-1)
#     check(pos+1, iend,pstart+left,pend-1)
#
# n = int(input())
# check1 = list(map(int,input().split()))
# check2 = list(map(int,input().split()))
# # print(check2[n-1])
# check(0,n-1,0,n-1)
# print()