import sys
from collections import Counter
arr = list(sys.stdin.readline().strip())
dic = Counter(arr)
ans = -1
num = 0
for i in range(10):
    if str(i) in dic:
        if i not in [6,9]:
            if dic[str(i)] > ans:
                ans = dic[str(i)]
        else:
            num += dic[str(i)]
a,b = divmod(num,2)
if b != 0:
    a+= 1
if ans > a:
    print(ans)
else:
    print(a)
