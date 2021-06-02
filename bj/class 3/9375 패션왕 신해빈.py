import sys

n = int(sys.stdin.readline())

for i in range(n):
    m = int(sys.stdin.readline())
    dic = dict()
    for _ in range(m):
        a,b = sys.stdin.readline().split()
        dic[b] = dic.get(b,1) +1

    ans = 1
    for i in dic.values():
        ans *= i
    print(ans -1)
