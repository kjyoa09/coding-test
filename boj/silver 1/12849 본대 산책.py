# DP
# 12850 본대 산책 2 전 풀어봄
# 피보나치 수열 느낌
from sys import stdin
stdin = open("in.txt")
input = stdin.readline
N = int(input())
#0 : 정보 과학관
#1 : 전산관
#2 : 미래관
#3 : 신앙관
#4 : 한경직 기념관
#5 : 진리관
#6 : 학생회관
#7 : 형남 공학관
maps = [1] + [0]*7
for i in range(N):
    maps = [maps[1]+maps[2],
            maps[0]+maps[2]+maps[3],
            maps[0]+maps[1]+maps[3]+maps[4],
            maps[1]+maps[2]+maps[4]+maps[5],
            maps[2]+maps[3]+maps[5]+maps[7],
            maps[3]+maps[4]+maps[6],
            maps[5]+maps[7],
            maps[4]+maps[6]]
print(maps[0]%1_000_000_007)