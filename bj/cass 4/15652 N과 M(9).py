# 중복처리할 때 Not in 별로 >> 차라리 defaultdict 활용한 해쉬처리
import sys
from collections import defaultdict
sys.stdin = open("in.txt")
N,M = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()

ans = defaultdict(int)

def pp(arr,li):
    global ans
    if len(arr) == M :
        ans[tuple(arr)] = 1
        return
    else:
        for idx,tmp in enumerate(li):
            pp(arr + [tmp], li[:idx] + li[idx+1:])

pp([],arr)

print(ans)

for i in ans:
    print(" ".join(map(str,i)))
