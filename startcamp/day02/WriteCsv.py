lunch = {
    '용성돌솥비빔밥':'054-444-2222',
    '별난짬뽕' : '054-473-4441',
    '돈까스' : '054-471-2222'
}
import csv
with open('lunch.csv','w',encoding = 'utf8',newline = '') as f:
    c = csv.writer(f)
    # for item in lunch.items() :
    #     f.write(f'{item[0]},{item[1]}\n')
    for item in lunch.items():
        c.writerow(item)
