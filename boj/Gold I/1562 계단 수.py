# DP
# 비트마킹 0-9 까지 2진수로 표시하고 각 값을 사용하면 표시
# 3차원 list 만들 때 [0]*10 for _ in range >> 이런 식으로 만들면 값이 같이 변함
from sys import stdin
stdin = open("in.txt")
input = stdin.readline
N = int(input())
maps = [[[0 for _ in range(1024)] for __ in range(10)] for ___ in range(101)]
for i in range(1,10):
    maps[1][i][2**i] = 1
for r in range(1,100):
    for c in range(10):
        for bit in range(1024):
            if maps[r][c][bit] == 0:
                continue
            else:
                tmp = bin(bit)[2:].rjust(10,"0")
                tmp = list(tmp[::-1])
                if c == 0:
                    tmp[1] = "1"
                    maps[r+1][1][int("".join(tmp[::-1]),2)] += maps[r][c][bit]
                elif c == 9:
                    tmp[8] = "1"
                    maps[r+1][8][int("".join(tmp[::-1]),2)] += maps[r][c][bit]
                else:
                    if tmp[c-1] == "0":                    
                        tmp[c-1] = "1"
                        maps[r+1][c-1][int("".join(tmp[::-1]),2)] += maps[r][c][bit]
                        tmp[c-1] = "0"
                    else:
                        maps[r+1][c-1][int("".join(tmp[::-1]),2)] += maps[r][c][bit]
                    if tmp[c+1] == "0":
                        tmp[c+1] = "1"
                        maps[r+1][c+1][int("".join(tmp[::-1]),2)] += maps[r][c][bit]
                        tmp[c+1] = "0"
                    else:
                        maps[r+1][c+1][int("".join(tmp[::-1]),2)] += maps[r][c][bit]
print(sum(maps[N][i][1023] for i in range(10)) % 1_000_000_000)