l = ['3', '6', '9']
for i in range(1,int(input())+1):
    cnt = 0
    for j in l :
        cnt += str(i).count(j)
    if cnt > 0 :
        print('-'*cnt, end = ' ')
    else :
        print(f'{i} ',end='')