
class ftn:
    def __init__(self,maps,N):
        self.maps = maps
        self.N = N

    def u(self,maps):
        tmp = [maps[0]] + [[0] * self.N for _ in range(self.N - 1)]
        TF = [True] * self.N
        for r in range(self.N - 1):
            
