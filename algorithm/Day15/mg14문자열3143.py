for tc in range(int(input())) :
    a,b = input().split()
    k=a.count(b)
    print('#%d %d'%((tc+1),len(a)-len(b)*k+k))