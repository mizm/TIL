def chk(s1,s2) :
    c1 = [0]*26
    c2 = [0] * 26
    for i in s1 :
        c1[ord(i)-97] += 1
    for i in s2 :
        c2[ord(i)-97] += 1
    for i in range(26) :
        if c1[i] != c2[i] :
            return False
    return True
n = int(input())
k = []
for i in range(n):
    k.append(input().split())
# print(k)
# cnt = 0
# for i in range(n) :
#     for j in range(i+1,n) :
#         if chk(k[i],k[j]) :
#             cnt += 1
# print(cnt)
for i in k :
    if chk(i[0],i[1]) :
        print("%s & %s are anagrams."%(i[0],i[1]))
    else :
        print("%s & %s are NOT anagrams." % (i[0], i[1]))