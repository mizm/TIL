with open('ssafy.txt','r',encoding = 'utf8') as f:
    lines = f.readlines()
lines.reverse()
with open('saffy_reverse.txt','w',encoding = 'utf8') as f:
    for i in lines :
        f.write(i)

