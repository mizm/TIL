max_m = int(input())
n = int(input())
Data = list(map(int,input().split()))
my_max = 0
temp_sum = 0
def DFS(pos) :
    global my_max,temp_sum
    if pos >= n :
        return
    if temp_sum > max_m :
        return
    if temp_sum > my_max :
        my_max = temp_sum

    temp_sum += Data[pos]
    DFS(pos+1)
    temp_sum-=Data[pos]
    DFS(pos + 1)
DFS(0)
print(my_max)