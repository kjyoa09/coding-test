from sys import stdin
stdin = open('in.txt')
input = stdin.readline

N = int(input())
arr = list(map(int,input().split(' ')))
maps = [[0] * N for _ in range(N)]

