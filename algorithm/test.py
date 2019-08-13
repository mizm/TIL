import sys


FH = open('eft0.dat','rb')
cnt = 0
while cnt <= 10000 :
    cnt += 1
    s = FH.read(1)
    if s == '': break
    print(s)
    if cnt % 1000 :
        print()
