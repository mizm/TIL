def searchmin(sbinary,allmap) :
    

for a in range(int(input())) : #총 테스트 케이스의 개수 T
    n = int(input()) #테스트케이스 n*n
        s =[list(map(int,input().split())) for i in range(n)] #행렬 생성
        t = 2**n # t binary를 위한 변수
        m = k = 160001 # 시너지의 최대값 20000 * 갯수 8
        for i in range(t) : #바이너리 검색
            sbinary = bin(i)[2:].zfill(t)
            if sbinary.count('1') == n//2 : # 반으로 정확히 나눠진경우
            k = searchmin(sbinary,s)
            if m > k :
                m = k
    print{f'#{a+1} {m}'}
