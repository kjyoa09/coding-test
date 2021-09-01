'''
너무 무식하게 푼 것 같기도;;
RB 중 먼저 움직이는 순서 파악

4 5
#####
#.BR#
#.O##
#####
'''
import heapq as hq
class ftn:
    def __init__(self,R,C,maps):
        self.R,self.C = R,C
        self.dic = {}
        for r in range(R):
            for c in range(C):
                if maps[r][c] == "#":
                    self.dic[(r,c)] = False
                else:
                    self.dic[(r,c)] = True
                
                if maps[r][c] == "R":
                    self.Red = (r,c)
                if maps[r][c] == "B":
                    self.Blue = (r,c)
                if maps[r][c] == "O":
                    self.Out = (r,c)

    def move(self,dx,dy,st,check = (-1,-1)):
        
        nx,ny = st
        while 1:
            px,py = nx+dx,ny+dy
            if self.dic[(px,py)]:                
                if (px,py) == self.Out:
                    return (px,py)
                elif (px,py) == check:
                    return (nx,ny)
                else:
                    nx,ny = px,py
            else:
                return (nx,ny)




    def bfs(self):
        start = (self.Red,self.Blue)
        visit = {start : 0}
        Dx,Dy = [0,1,0,-1],[1,0,-1,0]
        que = [(0,start)]
        
        while que:
            cnt,(red,blue) = hq.heappop(que)
            if cnt >= 10 :
                break

            if not visit.get((red,blue),False):
                visit[(red,blue)] = cnt
                for idx in range(4):
                    dx,dy = Dx[idx],Dy[idx]
                    if dx == 0:
                        if dy == 1:
                            if red[1] > blue[1]:
                                pred = self.move(dx,dy,red)
                                pblue = self.move(dx,dy,blue,pred)

                            else:
                                pblue = self.move(dx,dy,blue)
                                pred = self.move(dx,dy,red,pblue)

                        else:
                            if red[1] > blue[1]:
                                pblue = self.move(dx,dy,blue)
                                pred = self.move(dx,dy,red,pblue)

                            else :
                                pred = self.move(dx,dy,red)
                                pblue = self.move(dx,dy,blue,pred)

                    else:
                        if dx == 1:
                            if red[0] > blue[0]:
                                pred = self.move(dx,dy,red)
                                pblue = self.move(dx,dy,blue,pred)
                            else : 
                                pblue = self.move(dx,dy,blue)
                                pred = self.move(dx,dy,red,pblue)
                        else:
                            if red[0] > blue[0]:
                                pblue = self.move(dx,dy,blue)
                                pred = self.move(dx,dy,red,pblue)
                            else:
                                pred = self.move(dx,dy,red)
                                pblue = self.move(dx,dy,blue,pred)

                    if pblue == self.Out or pred == pblue:
                        continue
                    elif pred == self.Out:
                        return cnt + 1
                    else :
                        hq.heappush(que,(cnt+1,(pred,pblue)))
        
        return -1      


from sys import stdin
stdin = open('in.txt')
input = stdin.readline
R,C = map(int,input().split(' '))
maps = [list(input().strip()) for _ in range(R)]

sol = ftn(R,C,maps)
print(sol.bfs())