n = int(input())
for i in range(n):
    tmp = list(input())
    ans = 0
    cnt = 0
    while tmp:
        a = tmp.pop(0)
        if a == "O":
            cnt += 1
            ans += cnt
        else: cnt = 0

    print(ans)
