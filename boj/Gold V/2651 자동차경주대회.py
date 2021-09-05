# dp
# 거리에 따라 최소 시간을 저장[최대 정비를 받지 않고 갈 수 있는 최대 거리]
# >> 리스트를 활용해서 저장할 경우 메모리 초과 
# >> dict 활용
from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
N = int(input());M = int(input())

dis = list(map(int,input().rstrip().split()))
cost = list(map(int,input().rstrip().split()))
inf = float("INF")
maps = dict()
check = [dis[0]]
maps[check[0]] = [0,[]]

for i in range(M):
    tmp_ch = [dis[i+1]]
    tmp_maps = dict()
    tmp_maps[dis[i+1]] = [inf,[]]
    for ch in check:
        if ch + dis[i+1] <= N:
            value = tmp_maps.get(ch + dis[i+1],[inf,inf])
            if value[0] > maps[ch][0]:# 정류소 안들려도 됨
                tmp_maps[ch + dis[i+1]] = maps[ch]
                tmp_ch += [ch + dis[i+1]]
        if tmp_maps[dis[i+1]][0] > maps[ch][0] + cost[i] : # 정류소 그냥 들림
            tmp_maps[dis[i+1]] = [maps[ch][0] + cost[i],maps[ch][1] + [i+1]]
    check = tmp_ch 
    maps = tmp_maps

ans = [inf,[]]
for ch in check:
    if maps[ch][0] < ans[0]:
        ans = maps[ch]
print(ans[0])
print(len(ans[1]))
for i in ans[1]:
    print(i,end = " ")

'''
메모리 초과
from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
N = int(input());M = int(input())

dis = list(map(int,input().rstrip().split()))
cost = list(map(int,input().rstrip().split()))
inf = float("INF")
maps = [[inf,[]] for _ in range(N+1)]
check = [dis[0]]
maps[check[0]] = [0,[]]

for i in range(M):
    tmp_ch = [dis[i+1]]
    tmp_maps = [[inf,[]] for _ in range(N+1)]
    for ch in check:
        if ch + dis[i+1] <= N and tmp_maps[ch + dis[i+1]][0] > maps[ch][0]: # 정류소 안들려도 됨
            tmp_maps[ch + dis[i+1]] = maps[ch]
            tmp_ch += [ch + dis[i+1]]
        if tmp_maps[dis[i+1]][0] > maps[ch][0] + cost[i] : # 정류소 그냥 들림
            tmp_maps[dis[i+1]] = [maps[ch][0] + cost[i],maps[ch][1] + [i+1]]
    check = tmp_ch 
    maps = tmp_maps

ans = [inf,[]]
for ch in check:
    if maps[ch][0] < ans[0]:
        ans = maps[ch]
print(ans[0])
print(len(ans[1]))
for i in ans[1]:
    print(i,end = " ")
'''