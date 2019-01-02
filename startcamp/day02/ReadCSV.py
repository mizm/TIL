
import csv
with open('lunch.csv','r',encoding = 'utf8') as f:
    items = csv.reader(f)
    for item in items :
        print(item)
    #lines = f.readlines()
    #for line in lines :
    #    print(line.strip().split(','))