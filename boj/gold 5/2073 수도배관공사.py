from sys import stdin
stdin = open("in.txt","r")
D,P = map(int,stdin.readline().rstrip().split())
ch = [-1] * (D + 1)
for _ in range(P):
    L,C = map(int,stdin.readline().rstrip().split())
    if L <= D:
        for i in range(D-L,-1,-1):
            if 0<= i <= D and ch[i] != -1:
                if ch[i+L] < min(ch[i],C):
                    ch[i+L] = min(ch[i],C)
        if ch[L] < C:
            ch[L] = C
print(ch[-1])