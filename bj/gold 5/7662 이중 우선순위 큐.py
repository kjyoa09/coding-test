import sys; 
import heapq as hq

T = int(sys.stdin.readline())
for _ in range(T):
    minH,maxH = [],[]
    visit = [False] * 1000000
    n = int(sys.stdin.readline())

    for idx in range(n):
        com,value = sys.stdin.readline().split()
        if com == "I":
            hq.heappush(maxH,(-int(value),idx))
            hq.heappush(minH,(int(value),idx))
            visit[idx] = True
        else:
            if value == "-1":
                while minH :
                    a,b = hq.heappop(minH)
                    if visit[b]:
                        visit[b] = False
                        break
            else:
                while maxH:
                    a,b = hq.heappop(maxH)
                    if visit[b]:
                        visit[b] = False
                        break

    ans = []
    while maxH:
        a,b = hq.heappop(maxH)
        if visit[b]:
            ans += [-a]
            break
    while minH:
        a,b = hq.heappop(minH)
        if visit[b]:
            ans += [a]
            break
    if len(ans) == 0:
        print("EMPTY")
    else:
        for i in ans:
            print(i, end = " ")

