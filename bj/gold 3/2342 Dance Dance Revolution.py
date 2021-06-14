# DP.. 맞나.. 애매하네;; : 완전탐색에 가까운 느낌인데;;
# 같은 알고리즘인데 일반 (l,r,v)로 구성된 list로 풀면 메모리 초과 
# >> 메모리 관리 측면도 생각 : 1차원으로 푸는 것 보다는 고차원으로 푸는 것이 좋은가.?
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


'''
from sys import stdin
arr = list(map(int,stdin.readline().rstrip().split()))

RF = [(0,0,0)]

dic = {(0,1):2,(0,2):2,(0,3):2,(0,4):2,
       (1,1):1,(1,2):3,(1,3):4,(1,4):3,
       (2,1):3,(2,2):1,(2,3):3,(2,4):4,
       (3,1):4,(3,2):3,(3,3):1,(3,4):3,
       (4,1):3,(4,2):4,(4,3):3,(4,4):1,}


for di in arr:
    if di == 0:
        break
    else:
        tmp = []
        for rf in RF:
            l,r,v = rf
            po = [dic[(l,di)],dic[(r,di)]]
            tmp += [(di,r,v+po[0]),(l,di,v+po[1])]
        RF = tmp
print(min([v for x,y,v in RF]))
'''