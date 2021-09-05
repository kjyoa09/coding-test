import sys
from collections import deque

M,N,H = map(int,sys.stdin.readline().rstrip().split())

maps = []

C_0 = 0
C_1 = deque([])
for h in range(H):
    tmp_map = []
    for n in range(N):
        tmp = sys.stdin.readline().rstrip().split()
        for idx,m in enumerate(tmp):
            if m == "0":
                C_0 += 1
            elif m== "1":
                C_1.append((h,n,idx,0))
        tmp_map += [tmp]
    maps += [tmp_map]


dh = [1,-1,0,0,0,0]
dn = [0,0,1,-1,0,0]
dm = [0,0,0,0,1,-1]

ans = -1

while C_1:
    h,n,m,day= C_1.popleft()

    for i in range(6):
        ph,pn,pm = h+dh[i],n+dn[i],m+dm[i]

        if 0<= ph < H and 0<= pn < N and 0<= pm < M and maps[ph][pn][pm] == "0":
            maps[ph][pn][pm] = "1"
            C_1.append((ph,pn,pm,day+1))
            C_0 -=1

    if ans < day:
        ans = day

if C_0 != 0:
    print(-1)
else:
    print(ans)

                
