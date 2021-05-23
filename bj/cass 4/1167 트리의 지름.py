# 첫 다익스트라로 임의의 노드(편의상 1번으로 함)에서 가장 끝 노드 찾기
# 찾은 노드에서 가장 먼 값 찾기
import sys
from collections import defaultdict,deque
import heapq as hq
sys.stdin = open("in.txt","r")

V = int(sys.stdin.readline())

dic = defaultdict(list)

for _ in range(V):
    tmp = deque(list(map(int,sys.stdin.readline().rstrip().split())))
    s = tmp.popleft()
    while tmp[0] != -1:
        e,v = tmp.popleft(),tmp.popleft()
        dic[s].append((v,e))


inf = float("INF")

def fi(start):
    tot_MAX = - inf
    visit = [inf] * (V+1)
    visit[start] = 0
    que = [(0,start)]

    while que:
        v,s = hq.heappop(que)
        for value,e in dic[s]:
            if visit[e] > v + value:
                visit[e] = v + value
                hq.heappush(que,(visit[e],e))
                if tot_MAX < visit[e]:
                    tot_MAX = visit[e]
    return tot_MAX,visit[1:]

_,A = fi(1)
print(fi(A.index(max(A))+1)[0])