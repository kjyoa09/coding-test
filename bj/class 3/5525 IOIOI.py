import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
P = list(sys.stdin.readline().strip())

patt = "I"+"OI"*n

T = len(patt)

ans = 0
k = 0
for i in range(m):

    if P[i] == patt[k]:
        k += 1
        if k == T:
            ans += 1
            k = T-2

    else:
        if P[i] == "I":
            k = 1
        else:
            k = 0
print(ans)
