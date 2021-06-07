# 통과 못함
# N * M * K 반복이여서 M이 가장 큰 것 찾아서 먼저 제거하는 식으로 코드 짬..
import sys
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    arr.append([a,b])
cnt = 0
ans = 0
while cnt != N-1:
    v = -1
    for i in range(len(arr)-1):
        tmp = arr[i][1]
        if tmp > v:
            v = tmp
            idx = i
    cnt+=1
    ans += arr[idx][0] * arr[idx][1] * arr[idx+1][1]
    arr[idx] = [arr[idx][0],arr[idx+1][1]]
    del arr[idx+1]
print(ans)

