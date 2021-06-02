ans = 1
for i in range(3):
    ans *= int(input())
ans = list(str(ans))
for i in range(0,10):
    print(ans.count(str(i)))
