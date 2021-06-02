import sys
from collections import Counter


n,m,b = map(int,sys.stdin.readline().strip().split())

arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
arr = [x for y in arr for x in y ]

dic = Counter(arr)

rt = max(dic.keys())
lt = min(dic.keys())
arr = dic.keys()

ans = []
for i in range(rt,lt-1,-1):

    tmp1 = sum([dic[x]*(x-i) for x in arr if x > i]) #제거 개수
    tmp2 = sum([dic[x]*(i-x) for x in arr if x < i]) #추가 개수
    if tmp2 > tmp1 + b:
        continue
    else:
        ans += [[i,tmp1 * 2 + tmp2]]
ans.sort(key = lambda x:(x[1],-x[0]))
print(ans[0][1],ans[0][0])
