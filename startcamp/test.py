a = input()
a = a.upper()
dic = {}
for c in a :
    if c in dic :
        dic[c] = dic[c] + 1
    else :
        dic[c] = 1
dic = sorted(dic.items(), key=lambda t : t[1])
if(len(dic) == 1) : print(dic[0][0])
else :
    if(dic[len(dic)-1][1] == dic[len(dic)-2][1]) :
        print("?")
    else :
        print(dic[len(dic)-1][0])

