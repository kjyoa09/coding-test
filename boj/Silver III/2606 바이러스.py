import sys

n = int(sys.stdin.readline())
r = int(sys.stdin.readline())

dic = {k:[] for k in range(1,n + 1)}
for _ in range(r):
    
    a,b = map(int,sys.stdin.readline().split())
    dic[a] += [b]
    dic[b] += [a]

visit = [1]
Q = [1]

while Q:
    tmp = Q.pop(0)
    nextQ = [x for x in dic[tmp] if x not in visit]
    Q += nextQ
    visit += nextQ
print(len(visit) - 1)
