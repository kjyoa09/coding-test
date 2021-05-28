# 1[root]에서 다익스트라 
# 이후 각 노드에서 갈 수 있는 노드 중 1에서 가장 가까운 값
import sys,heapq as hq

sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())

dic = {i : [] for i in range(1,N+1)}
while 1:
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    if tmp == []:
        break
    else:
        s,e = tmp
        dic[s].append((1,e))
        dic[e].append((1,s))


visit = [True] * (N + 1)
li = [float("INF")] * (N + 1)
li[1] = 0

que = [(0,1)]

while que:
    v,s = hq.heappop(que)
    if visit[s] :
        visit[s] = False
        for cost,e in dic[s]:
            if li[e] > cost + v:
                li[e] = cost + v
                hq.heappush(que,(cost + v,e))

for i in range(2,N+1):
    tmp = [[x[1],li[x[1]]] for x in dic[i]]
    tmp.sort(key = lambda x:x[1])
    print(tmp[0][0])