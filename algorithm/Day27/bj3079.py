# print(30//7)
# print(30//10)
n,k = map(int,input().split())
item = []
m = 0
for i in range(n):
    item.append(int(input()))
    if m < item[i] :
        m = item[i]

st = 1
ed = m*k
result = 789654321
while st <= ed :
    mid = (st+ed)//2
    total = 0
    for i in item :
        total += mid // i
    if total < k :
        st = mid + 1
    else :
        ed = mid - 1
        # if result > mid :
        #     result = mid
print(ed+1)