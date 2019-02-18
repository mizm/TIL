import sys

sys.stdin = open("D03_ex2_input.txt", 'r')

Data = list(map(int,input().split()))
n = len(Data)
result = False
print(Data)
for i in range(1,1 << n) :
    item = []
    for j in range(n) :
        if i & (1 << j) :
            item.append(Data[j])
    print(item)
    # if len(item) == 5 and sum(item) == 0 :
    #     # print(item)
    #     result = True
    #     break
# print(result)