# def bubblesort(a) :
#     for j in range(1,len(a)):
#         for i in range(len(a)-j) :
#             if a[i] > a[i+1] :
#                 a[i],a[i+1] = a[i+1],a[i]
#     return a
#
# print(bubblesort([1,5,4,3,2]))

def bubble(a) :
    all = len(a)
    for now in range(all-1) :
        for next in range(now+1, all) :
            if a[next] < a[now] :
                a[next],a[now] = a[now],a[next]

    return a

print(bubble([1,4,5,3,2]))