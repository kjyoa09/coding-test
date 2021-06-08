import sys

N,r,c = map(int,sys.stdin.readline().strip().split())

count = 0
tli = [1]
for i in range(N):
    tli.append(tli[i]*2)
while N:
    if r >= tli[N-1]:
        r -= tli[N-1]
        count += (tli[N] * tli[N-1])
    if c >= tli[N-1]:
        c -= tli[N-1]
        count += (tli[N-1] ** 2)
    N -= 1

print(count)
