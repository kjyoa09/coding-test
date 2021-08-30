from sys import stdin
import heapq as hq

stdin = open("in.txt")
input = stdin.readline
que = []

N = int(input())
W = [list(map(int,input().split(' '))) for _ in range(N)]

dp = [[float("INF")]  * N for _ in range(int('1'+'0'*N,2))] # dp[i][j] : i그룹 j 끝점 최소



print(dp)