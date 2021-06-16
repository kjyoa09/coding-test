import sys

sys.stdin = open("in.txt","r")
N,M = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()

def pp(path,ls):

    if len(path) == M:
        path = list(map(str,path))
        print(" ".join(path))
        return
    
    for idx,tmp in enumerate(ls):
        pp(path + [tmp],ls[:idx] + ls[idx+1:])


pp([],arr)