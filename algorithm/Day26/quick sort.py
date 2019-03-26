data = [11,45,23,81,28,34]
# data = [11,45,22,81,23,34,99,22,17,8]
# data = [1,1,1,1,1,0,0,0,0,0]
def partion(f,t) :
    pivot = data[(f + t) // 2]
    i = f
    j = t
    while i < j:
        while i < j and data[i] <= pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    # data[f],data[j] = data[j],data[f]
    return i
def quicksort(f,t) :
    if f < t :
        i = partion(f,t)
        quicksort(f,i-1)
        quicksort(i+1,t)

quicksort(0,len(data)-1)
print(data)
