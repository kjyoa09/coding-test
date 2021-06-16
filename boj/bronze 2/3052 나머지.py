ans = []
for i in range(10):
    tmp = int(input()) % 42
    if tmp not in ans:
        ans += [tmp]
print(len(ans))
