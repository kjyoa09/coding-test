# 에라토스테네스의 체 활용해서 N 이하 소수 찾기
# two pointers 사용해서 구간 합 구하기
# 소수 문제 풀때 N=1일 때 예외처리 잘하기
from sys import stdin
stdin = open("in.txt","r")
N = int(stdin.readline())
if N == 1:
    print(0)
else:
    prime = []
    ch = [True] * (N+1)
    for i in range(2,N+1):
        if ch[i]:
            prime += [i]
            for num in range(i+i,N+1,i):
                ch[num] = False
    lt = 0;rt = 0
    v = prime[0]
    ans = 0
    while lt<=rt<len(prime):
        if v > N:
            v -= prime[lt]
            lt += 1
        elif v < N:
            rt += 1
            if rt < len(prime):
                v += prime[rt]
        else:
            ans +=1
    #       print(lt,rt)
            rt += 1
            if rt < len(prime):
                v += prime[rt]
    #print(prime)
    print(ans)