# move : 각 열or행을 arr로 받아서 계산 >> TF로 앞의 값 계산 여부 확인
# direct : 방향설정 >> 방향에 따라 0위치 달라짐
#          D 에서 x를 거꾸로 넣어주지 않아서 틀렸었음
# find : 모든 방향에 대해서 진행 후 가장 큰 값 찾음
#        값이 줄어드는 경우는 없어서 5번 진행하고 가장 큰 값 찾기
#        재귀호출

class ftn:
    def __init__(self,maps,N):
        self.maps = maps
        self.N = N
        self.ans = 0

    def move(self,arr):
        re,TF = [],True
        for x in arr:
            if not x: # 0이면 continue
                continue
            else:
                if TF: # 앞에 계산되었으면
                    re.append(x)
                    TF = False
                else:
                    if re[-1] == x: # 앞이랑 같으면
                        re[-1] += x
                        TF = True
                    else: # 같지 않으면
                        re.append(x)
        return re

    def direct(self,di,maps):
        re = []
        if di == "U":
            for x in zip(*maps):
                tmp = self.move(x)
                re.append(tmp + [0] * (self.N-len(tmp)))
            return list(map(list,zip(*re)))

        elif di == "D":
            for x in zip(*maps):
                tmp = self.move(x[::-1])
                re.append([0] * (self.N-len(tmp)) + tmp[::-1])
            return list(map(list,zip(*re)))

        elif di == "L":
            for x in maps:
                tmp = self.move(x)
                re.append(tmp + [0] * (self.N-len(tmp)))
            return re

        elif di == "R":
            for x in maps:
                tmp = self.move(x[::-1])
                re.append([0] * (self.N-len(tmp)) + tmp[::-1])
            return re

    def find(self,maps,cnt):
        if cnt == 5:
            tmp = max(x for y in maps for x in y)
            if tmp > self.ans:
                self.ans = tmp
        else:
            for di in ["U","D","R","L"]:
                self.find(self.direct(di,maps),cnt + 1)


from sys import stdin
stdin = open('in.txt')
input = stdin.readline
N = int(input())
maps = [list(map(int,input().strip().split(' '))) for _ in range(N)]


sol = ftn(maps,N)
sol.find(sol.maps,0)
print(sol.ans)