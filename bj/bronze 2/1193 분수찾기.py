n = int(input())
i = 1
s = 0
while s < n:
    s += i
    i += 1
if i % 2 == 0:
    n = s - n
    print(str(n + 1)+"/" + str(i-n -1))
else:
    n = abs(n-s)
    print(str(i-n - 1) + "/" + str(n + 1))
