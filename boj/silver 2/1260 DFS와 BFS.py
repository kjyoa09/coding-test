import sys
n,m,v = map(int,sys.stdin.readline().split())

dic = {k:list() for k in range(1,n+1)}

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if b in dic[a]:
        continue
    else:
        dic[a] += [b]
        dic[b] += [a]

for i in dic.keys():
    dic[i].sort()


stack = [v]
dfs = []

while stack:
    tmp = stack.pop(0)
    if tmp not in dfs:
        dfs += [tmp]
        stack = dic[tmp] + stack

for i in dfs:
    print(i, end = " ")
print()


bfs = [v] + dic[v]
Q = dic[v]
while Q:
    tmp = Q.pop(0)
    
    tmp = [x for x in dic[tmp] if x not in bfs]
    bfs += tmp
    Q += tmp

for i in bfs:
    print(i, end = " ")


