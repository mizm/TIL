# def mysqrt(n) :
#     if n == 1 :
#         return 1
#     a=b=0
#     for i in range(n):
#         if (i+1)**2 > n :
#             break
#     b = i+1
#     a = i
#     c = 0
#     while True :
#         if round(a**2,6) == round(b**2,6) :
#             return a
#         c = (a+b)/2
#         if c**2 > n :
#             b = c
#         else :
#             a = c
            
# def mysqrt(n,a,b) :
#     if n == 1 :
#         return 1
#     if a == 0 and b == 0 :
#         a=b=0
#         for i in range(n):
#             if (i+1)**2 > n :
#                 break
#         b = i+1
#         a = i
#         return mysqrt(n,a,b)

#     if round(a**2,6) == round(b**2,6) :
#         return a
#     c = 0
#     c = (a+b)/2
#     if c**2 > n :
#         b = c
#     else :
#         a = c
#     return mysqrt(n,a,b)
# print(mysqrt(5,0,0))

# from math import sqrt
# print(sqrt(5))
        
# print('111000'.count('1'))

import pandas as pd
items = {
    '공정명' : ['에칭','에칭','드릴','드릴']
    ,'설비명' : ['드릴1호','드릴2호','에칭1호','에칭1호']
    ,'작업시간' : ['11/23','11/24','11/25','11/26']
    ,'모델' : ['A','B','A','B']
    ,'기종' : ['BG','CS','BG','CS']
    ,'lot' : [1,2,1,3]
}
data = pd.DataFrame(items)
print(data)

pt = pd.pivot_table(data,index=['공정명'],columns=['기종','모델','lot'],values = ['기종','lot'],aggfunc='first')
print(pt.unstack())

# print('##################')
# pt1 = pd.pivot_table(data,index=['공정명'],columns=['기종'],values=['설비명','작업시간'],aggfunc='first')
# print(pt1)
print('##################')
grouped = data.groupby(['기종','모델','lot','공정명'])
print(grouped.first().unstack())
print(grouped.first())

print('##################')

print('##################')
print(groupd)
# print("################")
# gp = grouped.first().transpose()
# print(gp.columns)
# #pt2 = pd.pivot_table(data,index=['공정명'],values=['설비명','작업시간'])
# #print(pt2)
# print("################")
# # pt = pd.pivot_table(grouped.first().groupby(['설비명','작업시간']),index=['공정명'],columns=['기종','모델','lot'],values = ['설비명','작업시간'],aggfunc='first')
# # print(pt)
