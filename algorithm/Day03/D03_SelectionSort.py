data = [1,3,9,44,5,2,14,55,7]

n = len(data)
for i in range(n) :
    my_min = i
    for j in range(i+1,n) :
        if data[j] <  data[my_min] :
            my_min = j
    data[i], data[my_min] = data[my_min], data[i]
print(data)