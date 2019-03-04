def makePi(pattern) :
    piTable = [0] * len(pattern)
    j = 0
    for i in range(1,len(pattern)) :
        while pattern[i] != pattern[j] :
            if j == 0 :
                piTable[i] = j
                break
            j = piTable[j-1]
        if pattern[i] == pattern[j] :
            piTable[i] = j+1
            j+= 1
    return piTable

n = int(input())
item = input()
piTable = makePi(item)
print(piTable)
print(n-piTable[n-1])

# print(makePi('aabaaa'))
# print(makePi('abaaab'))
# print(makePi('baaaba'))
# print(makePi('aaaaa'))
# print(makePi('aabaaac'))
# [0, 1, 0, 1, 2, 2]
# [0, 0, 1, 1, 1, 2]
# [0, 0, 0, 0, 1, 2]
# [0, 1, 2, 3, 4]
# [0, 1, 0, 1, 2, 2, 0]
