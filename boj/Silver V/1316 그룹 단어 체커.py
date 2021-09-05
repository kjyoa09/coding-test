n = int(input())
ans = 0
for i in range(n):
    s = input()
    used = []
    for c in s:
        if c not in used or c == used[-1]:
            used += [c]
        else:
            break
    else:
        ans += 1
print(ans)