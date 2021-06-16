# Known이 변할 때까지 지속
# Known에 포함되면 다시 추가하지 않음.
import sys

sys.stdin = open("in.txt","r")
N,M = map(int,sys.stdin.readline().rstrip().split())

arr = list(map(int,sys.stdin.readline().rstrip().split()))
known = set(arr[1:])

stack = []
for _ in range(M):
    stack.append(set(list(map(int,sys.stdin.readline().rstrip().split()))[1:]))
while 1:
    tmp = []
    diff = False
    while stack:
        TMP_set = stack.pop()
        if TMP_set & known == set():
            tmp.append(TMP_set)
        else :
            known = known | TMP_set
            diff = True
    
    if diff :
        stack = tmp
    else:
        stack = tmp
        break
    
print(len(stack))