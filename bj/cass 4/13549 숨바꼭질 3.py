# 0부터 시작임
# K 도착시 cnt값 저장 이후 cnt이상인 값은 push 안함.
import sys,heapq as hq

sys.stdin = open("in.txt","r")
N,K = map(int,sys.stdin.readline().rstrip().split())

que = [(0,N)]
inf = float("INF")
MAX = 100001
visit = [inf] * (MAX)
visit[N] = 0
tmp_value = inf

while que:
    cnt,now = hq.heappop(que)
    if 0 <= now -1 < MAX and visit[now - 1] > cnt + 1 and tmp_value > cnt + 1:
        visit[now - 1] = cnt + 1
        hq.heappush(que,(cnt + 1, now - 1))
        if now - 1 == K and tmp_value > cnt + 1 :
            tmp_value = cnt + 1
    if 0<= now + 1 < MAX and visit[now + 1] > cnt + 1 and tmp_value > cnt + 1:
        visit[now + 1] = cnt + 1
        hq.heappush(que,(cnt + 1, now + 1))        
        if now + 1 == K and tmp_value > cnt + 1 :

            tmp_value = cnt + 1
    while 1:
        now *= 2
        if now < MAX and visit[now] > cnt and tmp_value > cnt:
            visit[now] = cnt
            hq.heappush(que,(cnt,now))
            if now == K and tmp_value > cnt + 1:
                tmp_value = cnt           
        else:
            break
print(visit[K])