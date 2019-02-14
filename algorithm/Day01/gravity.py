temp = my_max = temp_max = 0
room = list(map(int,input().split()))

for i in range(len(room)) :
    if room[i] >= temp :
        temp = room[i]
        if my_max <= temp_max :
            my_max = temp_max
            temp_max = 0
    else :
        temp_max += 1
        if my_max < temp_max:
            my_max = temp_max
print(my_max)



