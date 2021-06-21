# 내 코드 : python 3 >> 시간 초과 [pypy로는 통과]
# 블로그 코드 : Knuth .. python 3 통과
# 같은 3중 for 문인 것 같은데 시간 차이가...
#  
#### 내가 작성한 코드
from sys import stdin
stdin = open("in.txt","r")
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    arr = list(map(int,stdin.readline().rstrip().split()))
    maps = [[float("INF")] * N for _ in range(N)]
    
    ch = [0,arr[0]]+[0]*(N-1)
    for i in range(N):
        maps[i][i] = arr[i]
        ch[i+1]=ch[i]+arr[i]

    for i in range(1,N): #Length
        for S in range(N-i): # 시작점
            for tmp in range(S,S+i):
                a = 0
                if S != tmp:
                    a += maps[S][tmp]
                if tmp +1 != S+i:
                    a += maps[tmp+1][S+i]
                if maps[S][S+i] > a:
                    maps[S][S+i] = a
            maps[S][S+i] += ch[S+i+1] - ch[S]
    print(maps[0][-1])
#### Knuth - optimization
#### https://blog.naver.com/hands731/221809346951
'''
import sys
sys.stdin = open("in.txt","r")
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    f = list(map(int, input().split()))
    s = [0]
    A = [[0] * (n+1) for _ in range(n)]
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        A[i-1][i] = i
        s.append(s[i-1]+f[i-1])

    for z in range(2, n+1):
        for i in range(n-z+1):
            j = i + z
            dp[i][j]=sys.maxsize           
            for k in range(A[i][j - 1], A[i + 1][j]+1):
                minn=dp[i][k]+dp[k][j]+s[j]-s[i]
                if dp[i][j]>minn:
                  dp[i][j]=minn
                  A[i][j]=k
         
    print(dp[0][n])
    for i in A:
        print(i)
    for i in dp:
        print(i)
'''