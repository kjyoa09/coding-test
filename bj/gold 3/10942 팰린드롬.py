# DP : maps[start+1][end-1] : 중간 구간이 팰린드롬이고 arr[start] == arr[end]면 start부터 end까지도 팰린드롬 
# INDEX 번호 잘 생각하기 : 길이가 N 까지 가능한데 range(3,N)으로 둬서 틀림

from sys import stdin
stdin = open("in.txt","r")
N = int(stdin.readline())
arr = list(map(int,stdin.readline().rstrip().split()))
maps = [[0] * N for _ in range(N)]
for i in range(N):
    maps[i][i] = 1
for i in range(N-1):
    if arr[i]==arr[i+1]:
        maps[i][i+1] = 1
for i in range(3,N+1):# 길이
    for start in range(N-i+1): # 시작점
        end = start + i -1 # 끝점
        if maps[start+1][end-1] == 1 and arr[start] == arr[end]: # maps[start+1][end-1] : 중간 구간
            maps[start][end] = 1
M = int(stdin.readline())
for _ in range(M):
    S,E = map(int,stdin.readline().rstrip().split())
    if maps[S-1][E-1]:
        print(1)
    else:
        print(0)

'''
# 문자열을 넣는것 자체로도 일단 메모리 초과
# 분할 정복 생각하고 작성 : 팰린드롬이라고 중심으로 나눈 두 부분이 팰린드롬이라는 생각 >> 틀린 이유


from sys import stdin
N = int(stdin.readline())
arr = list(map(int,stdin.readline().rstrip().split()))
maps = [[""] * N for _ in range(N)] # row : 길이 col : idx

for r in range(N):
    for c in range(N):
        if r == 0: #길이 == 1
            maps[r][c] = str(arr[c])
        else: 
            if r%2 == 1: # 숫자 개수 : 짝수 길이 r + 1 >> 시작점: c 끝점 : c+r+1 - r//2
                if c + r + 1 < N and  maps[r-1][c] != "" and  maps[r-1][c+r] != "" and maps[r-1][c] == maps[r-1][c+r//2+1][::-1]:
                    maps[r][c] = maps[r-1][c] + maps[r-1][c+r//2+1]
            else: # 숫자 개수 : 홀수
                if c + r + 1 < N+1 and maps[r-2][c] != "" and  maps[r-2][c+r] != "" and maps[r-2][c] == maps[r-2][c+r-2+1][::-1]:
                    maps[r][c] =  maps[r-2][c] + str(arr[c+r//2]) +  maps[r-2][c+r-2+1][::-1]

M = int(stdin.readline())
for _ in range(M):
    S,E = map(int,stdin.readline().rstrip().split())
    if maps[E-S][S-1] == "":
        print(0)
    else:
        print(1)
'''