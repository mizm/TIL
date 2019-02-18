data = [1,2,3,5,6,7,8,9,22,33,44]

start = 0
end = len(data)-1
middle = end//2
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None
print(binary_search(4,data))
check = 4
while start <= end :
    middle = (end+start)//2
    if data[middle] == check :
        print(middle)
        break
    elif data[middle] > check :
        end = middle -1
    else :
        start = middle + 1

print(False)