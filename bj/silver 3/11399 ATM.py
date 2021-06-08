_ = input()
arr = list(map(int,input().split()))
arr.sort()

ans = [0]

for i in arr:
    ans += [ans[-1] + i]
print(sum(ans))
