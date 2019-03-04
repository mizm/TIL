ch = { 'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9 }
for tc in range(int(input())) :
    input()
    item = input().split()
    temp = sorted(item, key = lambda item : ch[item])
    print('#{0}'.format(tc+1))
    print('{0}'.format(' '.join(temp)))