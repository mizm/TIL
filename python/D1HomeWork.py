n = int(input())
l = []
for i in range(n) :
    l.append(sum(map(lambda x: x if x%2 == 1 else 0  ,map(int,input().split()))))
for j in range(n) :
    print(f'#{j+1} {l[j]}')