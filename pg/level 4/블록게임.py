# 블록 별 삭제시 필요한 블록 좌표 구하기[self.need]
# self.need에 블록을 넣을 수 있으면 del

# 흠.. 시간 자체는 빠르게 나오기는 하는데.. 너무 난잡해 보이는 것 같기도..
# >> set add로 사용하려니 시간이 조금 더 걸리기는 함
from collections import defaultdict
class ftn:
    def __init__(self,board):
        self.N = len(board)
        self.board = [[True] * self.N for _ in range(self.N)]
        self.ans = 0
        self.dic = defaultdict(list)
        self.need = {}
        
        for r in range(self.N):
            for c in range(self.N):
                if board[r][c]:
                    self.dic[board[r][c]].append((r,c))
                    self.board[r][c] = False
        
        for k,v in self.dic.items():
            self.need[k] = list(set((x,y) for x in set(r[0] for r in v) for y in set(r[1] for r in v)) - set(v))
        
    def find(self):
        TF = False
        dL = []

        for k,v in self.need.items():
            if all(self.board[x][v[0][1]] for x in range(v[0][0]+1)) and all(self.board[x][v[1][1]] for x in range(v[1][0]+1)):
                TF = True
                self.ans += 1
                for vv in self.dic[k]:
                    self.board[vv[0]][vv[1]] = True
                dL.append(k)

        if TF:
            for d in dL:
                del self.dic[d]
                del self.need[d]
        return TF
        
def solution(board):
    sol = ftn(board)
    sol.find()
    while 1:
        if not sol.find():
            break
    return sol.ans