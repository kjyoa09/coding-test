# Flag를 통해서 찾으면 전부 Break
import sys
sys.setrecursionlimit(10**8)
sys.stdin = open("in.txt","r")
maps = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(9)]
dic_R = {r:[True] * 9 for r in range(9)}
dic_C = {c:[True] * 9 for c in range(9)}
dic_S = {(r,c):[True] * 9 for r in range(3) for c in range(3)}
zeros = 81
for r in range(9):
    for c in range(9):
        if maps[r][c] != 0:
            tmp = maps[r][c] - 1
            dic_R[r][tmp] = False
            dic_C[c][tmp] = False
            dic_S[(r//3,c//3)][tmp] = False
            zeros -=1
flag = False
def dfs(x,y,zeros):
    global flag
    if zeros == 0:
        for i in maps:
            print(int("".join(str(x) for x in i)))
        flag = True
        return flag
    if 0<=x<9 and 0<=y<9:
        if maps[x][y] == 0:
            for i in range(9):
                if dic_R[x][i] and dic_C[y][i] and dic_S[(x//3,y//3)][i]:
                    dic_R[x][i] = False;dic_C[y][i]= False;dic_S[(x//3,y//3)][i]= False
                    maps[x][y] = i+1
                    if y == 8:
                        dfs(x+1,0,zeros-1)
                    else:
                        dfs(x,y+1,zeros-1)
                    if flag :
                        break
                    dic_R[x][i] = True;dic_C[y][i]= True;dic_S[(x//3,y//3)][i]= True
                    maps[x][y] = 0
        else:                
            if y == 8:
                dfs(x+1,0,zeros)
            else:
                dfs(x,y+1,zeros)

dfs(0,0,zeros)