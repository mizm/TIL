# def solution(N, stages):
#     answer = []
#     temp = []
#     f = c = 0
#     for i in range(1,N+1) :
#         f = stages.count(i)
#         c = 0
#         if f > 0 :
#             for k in stages :
#                 if k >= i :
#                     c += 1
#         if c == 0 :
#             fail = 0
#         else :
#             fail = f/c
#         temp.append((i,fail))
#         temp = sorted(temp,key=lambda t : t[1],reverse = True)
#     for i,k in temp :
#         answer.append(i)
#     return answer
# print(solution(4,[4,4,4,4,4]))
# solution(5,[2,1,2,6,2,4,3,3])
# a = [1,2,3]
# b = [[1,
# 3,4],[3,4,5]]
# def check(a,b) :
#     for j in b :
#         chk = 0
#         for i in a :
#             if i in j :
#                 chk += 1
#                 continue
#             else :
#                 break
#         if chk == len(a) :
#             return False
#     return True
# print(check(a,b))
# def check(a,b) :
#     for j in b :
        
def search(item,trelation) :
    if len(item) == 1:
        for k in trelation[item[0]] :
            if trelation[item[0]].count(k) == 1:
                continue
            else :
                return False
        return True
    elif len(item) > 1 :
        t = item.pop()
        temp = trelation[t]
        for i in item :
            temp = list(zip(temp,trelation[i]))
        for i in temp :
            if temp.count(i) == 1:
                continue
            else :
                return False
        return True
# def dfs(pos,item,n,answer_list,answer,trelation) :
#     temp = item[:]
#     if pos == n :
#         if len(item) > 0 :
#             if search(item,trelation) :
#                 if not item in answer_list :
#                     answer_list.append(item)
#     else :
#         temp.append(pos)
#         dfs(pos+1,temp,n,answer_list,answer,trelation)
#         temp1 = item[:]
#         dfs(pos+1,temp1,n,answer_list,answer,trelation)

def solution(relation):
    n = len(relation[0])
    trelation = [[] for i in range(n)]
    answer_list = []
    answer = 0
    for i in relation :
        for idx,j in enumerate(i) :
            trelation[idx].append(j)
    for i in range(2**n) :
        k = bin(i)[2:].zfill(n)
        item = []
        for idx,t in enumerate(k) :
            if t == '1' :
                item.append(idx)
        
        if search(item,trelation) :
            if item == [1] :
                print(search(item,trelation))
                answer_list.append(item)
    print(answer_list)
    return answer
relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]    
print(solution(relation))
trelation = [[5,6,7,8,9],['ryan', 'apeach', 'tube', 'con', 'muzi', 'apeach'],[5,4,3,2,1]]
item = [1]
print(search(item,trelation))