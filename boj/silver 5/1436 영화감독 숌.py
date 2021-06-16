import sys


n = int(input())


i = 665
cnt = 0
while cnt != n:
    i += 1
    if "666" in str(i):
        cnt += 1
print(i)
