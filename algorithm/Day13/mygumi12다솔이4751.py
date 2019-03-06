def f() :
    print('..#..', end='')
    [print('.#..', end='') for i in range(len(Data) - 1)]
    print()
def s():
    print('.', end='')
    [print('#.', end='') for i in range((len(Data)) * 2)]
    print()
for tc in range(int(input())) :
    Data = input()
    f()
    s()
    print('#',end='')
    [print('.{}.#'.format(Data[i]), end='') for i in range(len(Data))]
    print()
    s()
    f()