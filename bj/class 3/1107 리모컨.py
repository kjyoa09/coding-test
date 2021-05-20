# itertools 사용... 찝찝하네;;;

import sys
from itertools import product
sys.stdin = open("in.txt")

target = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ban = list(map(int,sys.stdin.readline().strip().split()))
use = list(map(str,[x for x in range(0,10) if x not in ban]))

ans = abs(target - 100)
if m == 10:
    print(ans)
else:
    for i in range(1,7):
        poss = list(product(use,repeat = i))
        tmp = min([abs(target-int(''.join(x))) for x in poss])

        if ans > tmp + i:
            ans = tmp + i
    print(ans)
