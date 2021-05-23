import sys

sys.stdin = open("in.txt","r")

N = int(sys.stdin.readline())
maps = []

for _ in range(N):
    maps.append(list(map(int,sys.stdin.readline().rstrip().split())))
print(maps)

start = [maps[0]]

for v in maps[1:]:
    tmp = start[-1]
    start.append([min(v[0] + tmp[1],v[0] + tmp[2]),
                  min(v[1] + tmp[0],v[1] + tmp[2]),
                  min(v[2] + tmp[1],v[2] + tmp[0])])

print(min(start[-1]))

        
