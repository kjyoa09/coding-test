import sys

sys.stdin = open("in.txt")
N,M = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()

def pp(arr,li):

    if len(arr) == M:
        print(" ".join(map(str,arr)))
        return
    else:
        for idx,tmp in enumerate(li):
            pp(arr + [tmp],li[idx:])

pp([],arr)