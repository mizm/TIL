counts = [0] * 12

item = 999999
tri = run = 0
for i in range(6) :
    counts[item % 10] += 1
    item //= 10
for i in range(10) :
    if counts[i] >= 3 :
        tri += (counts[i] // 3)
        counts[i] %= 3
    if counts[i] >= 1 and counts[i+1] and counts[i+2] :
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1

if tri + run >= 2 :
    print('baby')
else :
    print('fail')