import sys

sys.stdin = open("in.txt","r")
N,M = map(int,sys.stdin.readline().rstrip().split())


def pp(path):

    if len(path) == M:
        path = list(map(str,path))
        print(" ".join(path))
        return
    
    for tmp in range(path[-1] + 1 , N+1):

        pp(path + [tmp])


for i in range(1,N+1):
    pp([i])
