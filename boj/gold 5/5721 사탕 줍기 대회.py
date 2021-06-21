from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline

while 1:
    N,M = map(int,input().rstrip().split())
    if N == M == 0:
        break
    else:
        maps = [list(map(int,input().rstrip().split())) for _ in range(N)]

        ans = []
        for lis in maps:
            tmp = [0,0]
            for i in lis:
                tmp = [max(tmp),tmp[0]+i]
            ans += [max(tmp)]
        tmp = [0,0]
        for i in ans:
            tmp = [max(tmp),tmp[0]+i]
        print(max(tmp))
#        print(ans)
