ans = [-1,-1]

for i in range(9):
    can = int(input())
    if can > ans[-1]:
        ans = [i + 1,can]
for i in ans[::-1]:
    print(i)