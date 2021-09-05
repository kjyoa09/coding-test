a = int(input())
b = input()
ans = 0
for idx,x in enumerate(b[::-1]):
    tmp = int(x) * a
    print(tmp)
    ans += tmp * 10**idx
print(ans)