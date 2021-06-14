# 1149 RGB와 다른점 : 1번 집과 N번 집 고려해야함
# 1번집 색 고정 후 마지막 N 번집 색 고를 때 1번집과 다른 색 고르도록 유도 
# ex : 1번 Red N 번 value : [inf,num,num]
from sys import stdin
stdin = open("in.txt","r")
N = int(stdin.readline())
maps = [list(map(int,stdin.readline().rstrip().split())) for _ in range(N)]
inf = float("INF")
st = [[maps[0][0],inf,inf],[inf,maps[0][1],inf],[inf,inf,maps[0][2]]]
for i in range(1,N):
    if i == N-1:
        tmp = [[inf,maps[-1][1],maps[-1][2]],[maps[-1][0],inf,maps[-1][2]],[maps[-1][0],maps[-1][1],inf]]
    else:
        tmp = [maps[i],maps[i],maps[i]]
    for num in range(3):
        st[num] = [min(st[num][1],st[num][2])+tmp[num][0],min(st[num][0],st[num][2])+tmp[num][1],min(st[num][1],st[num][0])+tmp[num][2]]
print(min([x for y in st for x in y]))