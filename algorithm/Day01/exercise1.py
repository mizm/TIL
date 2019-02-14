import sys
sys.stdin = open('input.txt', 'r')

Data = list(map(int, input().split()))

print(Data)
my_max = my_idx = -1
now = 0
for d in Data :
    if my_max < d :
        my_max = d
        my_idx = now
    now += 1
print(my_max, my_idx+1)