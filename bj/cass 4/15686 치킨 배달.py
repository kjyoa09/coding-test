import sys

sys.stdin = open("in.txt","r")
N,M = map(int,sys.stdin.readline().rstrip().split())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]