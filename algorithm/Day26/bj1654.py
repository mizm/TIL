k, n = map(int,input().split())
data = []
for i in range(k) :
    data.append(int(input()))
max_v = max(data)
min_v = 1
while min_v <= max_v :
    to = 0
    mid = (max_v+min_v)//2
    for i in data :
        to += i//mid
    if to >= n :
        min_v = mid + 1
    else :
        max_v = mid - 1
print(max_v)
# p = sum(data) // n
# while p > 0 :
#     to = 0
#     for i in data :
#         to += i//p
#     if to == n : break
#     else :
#         print(to)
#         p-=1
# print(p)