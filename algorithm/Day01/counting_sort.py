data = [0,4,1,3,1,2,4,1]
sorted_data = [0]*8
counts = [0]*5
for i in data :
    counts[i] += 1
for j in range(1,len(counts)) :
    counts[j] += counts[j-1]
for d in data :
    sorted_data[counts[d]-1] = d
    counts[d] -= 1
print(sorted_data)