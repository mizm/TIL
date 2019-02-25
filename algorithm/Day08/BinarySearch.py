def search(want,start,end) :
    mid = (start+end) // 2
    if start > end :
        return -1
    if want == data[mid] :
        return mid
    if want > data[mid] :
        end = mid - 1
    if want < data[mid] :
        start = mid+1
    search(want,start,end)

data = [1,2,4,5,6,7,8]

print(search(5,0,6))