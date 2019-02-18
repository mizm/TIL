data = [1,2,3,5,6,7,8,9,22,33,44]

check = 5
temp = False
for i in range(len(data)) :
    if check == data[i] :
        temp = True
        break
if temp :
    print(i)
else :
    print(temp)