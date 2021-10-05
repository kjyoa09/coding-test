from sys import stdin,exit
stdin = open('in.txt','r')
input = stdin.readline

n,m = map(int,input().strip().split(' '))
maps = [list(input().strip()) for _ in range(n)]
dic = {}


if n == m == 1:
    x = int(maps[0][0])
    if x == ((x**(1/2))//1)**2:
        print(x)
    else:
        print(-1)
else:
    for r in range(n):
        for c in range(m):
            for dx in range(-n+1,n):
                for dy in range(-m + 1, m):
                    if dx == dy == 0:
                        continue
                    tmp = ''
                    x,y = r,c
                    while 0<=x<n and 0<=y<m:
                        tmp += maps[x][y]
                        dic[int(tmp)] = 1
                        x+=dx
                        y+=dy

    for x in sorted(dic.keys(),reverse=True):
        if x == ((x**(1/2))//1)**2:
            print(x)
            break
    else:
        print(-1)