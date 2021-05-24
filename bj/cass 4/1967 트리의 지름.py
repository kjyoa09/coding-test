# 1167번과 같은 문제
# 임의의 노드 하나 잡고 가장 먼 노드 찾고 그 노드에서 가장 먼 노드의 거리 >> 지름
import sys
import heapq as hq

sys.stdin = open("in.txt","r")

N = int(sys.stdin.readline())
maps = [[] for _ in range(N)]

while 1:
    try :
        s,e,v = map(int,sys.stdin.readline().rstrip().split())
        maps[s-1].append((v,e-1))
        maps[e-1].append((v,s-1))
    except:
        break

inf = float("INF")
def find(start):

    que = [(0,start)]
    visit = [inf] * N
    visit[start] = 0

    while que:
        value,start = hq.heappop(que)

        for cost,end in maps[start]:
            if visit[end] > value + cost:
                visit[end] = value + cost
                hq.heappush(que,(value + cost, end))
    
    return visit

tmp = find(0)
ans = find(tmp.index(max(tmp)))
print(max(ans))