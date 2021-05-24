# 벨만 포드 : 다익스트라 보다는 느리지만 음수 가중치가 있을 때 사용 가능
# 최단 거리일 경우 간선의 수는 N-1이다. 를 전제로 rep == N-1일 때 weight가 변할 경우 음의 순환이 있음.
# 문제에서는 음의 순환이 있는지 확인.

import sys
sys.stdin = open("in.txt","r")

TC = int(sys.stdin.readline())

inf = 2200000000
def fin(weight):
    result = False
    for rep in range(N):
        for node in range(N):
            for end,value in maps[node]:
                cost = value + weight[node]
                if weight[end] > cost:
                    weight[end] = cost
                    if rep == N-1:
                        result = True
                        break
    return result

for _ in range(TC):
    N,M,W = map(int,sys.stdin.readline().rstrip().split())
    maps = [[] for _ in range(N)]

    for __ in range(M):
        s,e,v = map(int,sys.stdin.readline().rstrip().split())
        maps[s-1].append((e-1,v))
        maps[e-1].append((s-1,v))
    for __ in range(W):
        s,e,v = map(int,sys.stdin.readline().rstrip().split())
        maps[s-1].append((e-1,-v))

    for i in range(N):
        if maps[i]:
            weight = [inf] * N
            weight[i] = 0
            if fin(weight):
                print("YES")
            else:
                print("NO")
            break