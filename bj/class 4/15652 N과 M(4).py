import sys

sys.stdin = open("in.txt")
N,M = map(int,sys.stdin.readline().rstrip().split())


def pp(num,arr):

    if len(arr) == M:
        print(" ".join(map(str,arr)))
        return
    else:
        for tmp in range(num,N+1):
            pp(tmp,arr + [tmp])

pp(1,[])