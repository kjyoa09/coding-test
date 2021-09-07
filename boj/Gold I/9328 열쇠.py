from collections import deque

class ftn:
    def __init__(self,h,w,maps,keys):
        self.h,self.w = h,w
        self.maps = maps
        self.check = [[True] * w for _ in range(h)]
        self.dic = {chr(i):False for i in range(65,91)}
        self.ans = 0

        for k in keys:
            if k == '0':
                break
            self.dic[k.upper()] = True

        self.que = deque([])
        
        for x in range(h):
            for y in range(w):
                if (x==h-1 or x==0 or y == 0 or y == w-1) and (maps[x][y] != '*'):
                    self.que.append((x,y))


                if maps[x][y] == "*":
                    self.check[x][y] = False
        
        

    def bfs(self):
        dx,dy,TF,nextque = [1,0,-1,0],[0,1,0,-1],False,deque([])

        while self.que:
            x,y = self.que.popleft()
            tmp = True

            if self.check[x][y]:
                self.check[x][y] = False
                if self.maps[x][y] == '.':
                    pass
                
                elif self.maps[x][y] == '$':
                    # print(x,y)
                    self.ans += 1
                
                elif 97<=ord(self.maps[x][y])<=122: #key
                    TF = True
                    self.dic[self.maps[x][y].upper()] = True
                else:
                    if self.dic[self.maps[x][y]]: #key 존재
                        pass
                    else: # key 없음
                        self.check[x][y] = True
                        nextque.append((x,y))
                        tmp = False
                
                if tmp:
                    for idx in range(4):
                        px,py = x + dx[idx], y + dy[idx]
                        if 0<=px<self.h and 0<=py<self.w and self.check[px][py] :
                            self.que.append((px,py))

        self.que = nextque
        return TF




from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

T = int(input())

for _ in range(T):
    h,w = map(int,input().split(' '))
    maps = [list(input().strip()) for _ in range(h)]
    keys = list(input().strip())
    sol = ftn(h,w,maps,keys)
    while 1:
        if not sol.bfs():
            break
    print(sol.ans)
    