from sys import stdin
stdin = open("in.txt")
input = stdin.readline
N = int(input())
maps = [[0] * 10 for _ in range(101)]
maps[1] = [0]+[1]*9
for r in range(1,100):
    for c in range(10):
        if c == 0:
            maps[r+1][1] += maps[r][0]
        elif c == 9:
            maps[r+1][8] += maps[r][9]
        else:
            maps[r+1][c-1] += maps[r][c]
            maps[r+1][c+1] += maps[r][c]
print(sum(maps[N])%1_000_000_000)
