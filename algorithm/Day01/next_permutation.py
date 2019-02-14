def next_permutation(permutation) :
    cand1 =  cand2 = -1
    # permutation=[3,2,5,4,1,6]
    n = len(permutation)
    for i in range(1,n) :
        if permutation[n-i] > permutation[n-i-1] :
            cand1 = n-i-1
            break
        # temp = check
    if cand1 == -1 :
        return False
    for i in range(n-1,cand1,-1) :
        if permutation[i] > permutation[cand1] :
            cand2 = i
            break
    permutation[cand1] ,  permutation[cand2] = permutation[cand2], permutation[cand1]

    permutation[cand1+1:] = permutation[:cand1:-1]

    return permutation

permutation=[3,2,5,4,1]
# print(next_permutation(permutation))

while(next_permutation(permutation)) :
    print(permutation)