from sys import stdin
import sys
sys.setrecursionlimit(10**6)
stdin = open("in.txt","r")

# 앞으로 갈 곳이 지나온 곳[순환 = 0]: 
# 앞으로 갈 곳이 지나온 곳[직선 = 1]
# 앞으로 갈 곳이 안 지나온 곳[-1]

def find(visit,idx,maps):
    global end,state
    next_idx = maps[idx]# 앞으로 갈 곳
    if maps[next_idx] == -1:
        state = False
        visit[idx] = 1
    else:
         
        if visit[next_idx] == -1 :
            visit[next_idx] = 0
            find(visit,next_idx,maps)
            maps[next_idx] = -1
            if state:
                if end == idx : 
                    state = False
            else:
                visit[idx] = 1   
        elif visit[next_idx] == 0: # 지나온 곳[순환]
            end = next_idx
            if next_idx != maps[next_idx] : #자기 자신 뽑은 사람
                state = True
        else: # 지나온 곳[직선]
            state = False
            visit[idx] = 1
T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    arr = [-1]*(N+1)
    maps = [0] + list(map(int,stdin.readline().rstrip().split()))
    for i in range(1,N+1):
        end = 0
        state = False
        if arr[i] == -1:
            arr[i] = 0
            find(arr,i,maps)
            maps[i] = -1
    print(sum(arr)+1)
    # print(maps)