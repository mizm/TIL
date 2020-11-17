import sys

sys.stdin = open('bj13458.txt','r')

import math
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
for i in A :
    N += math.ceil((i-B) / C) if (i-B) > 0 else 0
print(N)