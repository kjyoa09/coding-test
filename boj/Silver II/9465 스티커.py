# N == 1
import sys

sys.stdin = open("in.txt")

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    maps = []

    maps += [list(map(int,sys.stdin.readline().rstrip().split()))]
    maps += [list(map(int,sys.stdin.readline().rstrip().split()))]

    if n == 1:
        print(max(maps[0][0],maps[1][0]))
    else:
        start = [max(maps[0][0],maps[1][0]),maps[1][0] + maps[0][1] ,maps[0][0] + maps[1][1]]

        for i in range(2,n):
            start = [max(start),
            max(start[2],start[0]) + maps[0][i],
            max(start[1],start[0]) + maps[1][i]]
        print(max(start))