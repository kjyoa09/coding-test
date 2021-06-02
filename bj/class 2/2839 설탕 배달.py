num = int(input())
ans = float("INF")

c = num//5

for i in range(0,c+1):
    b = num - i*5
    if b % 3 == 0 and ans > i + b//3:
        ans = i + b//3
if ans == float("INF"):
    print(-1)
else:
    print(ans)
