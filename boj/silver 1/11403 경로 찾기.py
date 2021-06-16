import sys

n = int(sys.stdin.readline())
maps = []

for _ in range(n):
    tmp = list(sys.stdin.readline().split())
    maps += [[idx for idx,x in enumerate(tmp) if x == "1" ]]



def bfs(tmp):
    v = tmp[:]
    q = tmp[:]
    while q:
        next_ = maps[q.pop(0)]
        next_ = [x for x in next_ if x not in v]
        v += next_
        q += next_
    for i in range(n):
        if i in v:
            print(1,end = " ")
        else:
            print(0,end = " ")
    print()


for i in range(n):
    tmp = maps[i][:]
    bfs(tmp)
