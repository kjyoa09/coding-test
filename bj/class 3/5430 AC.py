import sys
from collections import deque
T =  int(sys.stdin.readline())

for _ in range(T):
    
    command = list(sys.stdin.readline().rstrip())
    n = sys.stdin.readline().rstrip()
    if n == "0":
        arr = list()
        sys.stdin.readline().rstrip()
    else:
        arr = sys.stdin.readline().rstrip()[1:-1].split(",")

    arr = deque(arr)
    direct = True   
    
    for tmp in command:
        if tmp == "R":
            direct = not direct
        else:
            if len(arr) == 0:
                print("error")
                break
            else:
                if direct:
                    arr.popleft()
                else:
                    arr.pop()
    else:
        arr =list(arr)
        if direct:
            print("["+",".join(arr)+"]")
        else:
            print("["+",".join(arr[::-1])+"]")
