# def partion(f,t) :
#     pivot = data[(f + t) // 2]
#     i = f
#     j = t
#     while i < j:
#         while data[i] < pivot:
#             i += 1
#         while data[j] > pivot:
#             j -= 1
#         if i < j:
#             data[i], data[j] = data[j], data[i]
#     # data[f],data[j] = data[j],data[f]
#     return i
# def quicksort(f,t) :
#     if f < t :
#         i = partion(f,t)
#         quicksort(f,i-1)
#         quicksort(i+1,t)
def partition(start, end):
    pivot = data[start]
    left = start + 1
    right = end
    done = False
    while left <= right:
        while left <= right and data[left] <= pivot:
            left += 1
        while left <= right and pivot <= data[right]:
            right -= 1
        if left<=right :
            data[left], data[right] = data[right], data[left]
    data[start], data[right] = data[right], data[start]
    return right


def quick_sort(start, end):
    if start < end:
        pivot = partition( start, end)
        quick_sort(start, pivot - 1)
        quick_sort( pivot + 1, end)
for tc in range(int(input())) :
    n = int(input())
    data = list(map(int,input().split()))
    quick_sort(0, len(data) - 1)
    # print(data)
    print("#%d %d"%(tc+1,data[n//2]))