import sys

n,k = map(int,sys.stdin.readline().strip().split())

if k <= n :
    print(n-k)
else:

    inf = float("INF")

    Visit = [inf] * (100001)
    Visit[n] = 0
    Q = [(0,n)]

    dx = [-1,1,2]
    while Q:
        cnt,now = Q.pop(0)

        post = [(cnt+1,now-1),(cnt+1,now+1),(cnt+1,now*2)]

        for i in post:
            if 0<= i[1] <= 100000 and Visit[i[1]] > i[0]:
                Visit[i[1]]= i[0]
                Q += [i]


    print(Visit[k])
