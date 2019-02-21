# def dfs(student) :
#     global result
#     if result :
#         return
#     # print(student)
#     if student == n :
#         result = 1
#         return
#     if student > n :
#         result = 0
#         return
#     dfs(student + a)
#     dfs(student + b)
#     dfs(student + c)
#
# a,b,c,n = list(map(int, input().split()))
# result = 0
# dfs(0)
# print(result)

a,b,c,n = list(map(int, input().split()))
def search() :
    for i in range(0,n+1) :
        tempa = a*i
        for j in range(0,n+1):
            tempb = b*j
            for k in range(0,n+1):
                tempc = c*k
                if tempa + tempb + tempc == n :
                    return 1
    return 0
print(search())