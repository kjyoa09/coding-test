from sys import stdin
stdin = open("in.txt","r")
arr = list(map(int,stdin.readline().rstrip().split()))
inf = float("INF")
RF = [[inf] * 5 for _ in range(5)]
RF[0][0] = 0

dic = {(0,1):2,(0,2):2,(0,3):2,(0,4):2,
       (1,1):1,(1,2):3,(1,3):4,(1,4):3,
       (2,1):3,(2,2):1,(2,3):3,(2,4):4,
       (3,1):4,(3,2):3,(3,3):1,(3,4):3,
       (4,1):3,(4,2):4,(4,3):3,(4,4):1,}


for di in arr:
    if di == 0:
        break
    else:
        tmp = [[inf] * 5 for _ in range(5)]
        for r in range(5):
            for l in range(5):
                if RF[r][l] != inf:
                    tmp[r][di] = min(tmp[r][di],RF[r][l] + dic[(l,di)])
                    tmp[di][l] = min(tmp[di][l],RF[r][l] + dic[(r,di)])
        RF = tmp
print(min([x for y in RF for x in y]))