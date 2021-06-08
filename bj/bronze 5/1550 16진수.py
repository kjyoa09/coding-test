import sys

input = sys.stdin.readline

dic = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

A = list(input().rstrip())

ans = 0
for idx,a in enumerate(A[::-1]):
    if a.isdigit():
        ans += int(a) * 16**idx
    else:
        ans += dic[a] * 16**idx
print(ans)

