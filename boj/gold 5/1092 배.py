from sys import stdin
from collections import deque
stdin = open("in.txt")
input = stdin.readline
N = int(input())
arr = list(map(int,input().rstrip().split()))
arr = deque(sorted(arr,reverse=True))
d = int(input())
maps = list(map(int,input().rstrip().split()))
maps = deque(sorted(maps,reverse=True))

if maps[0] > arr[0]:
    print(-1)
else:
    ans = 0
    while maps:
        save_arr = deque([])
        while arr:
            remain = deque([])
            tmp_arr = arr.popleft()            
            while maps:
                tmp = maps.popleft()
                if tmp <= tmp_arr:
                    save_arr.append(tmp_arr)
                    break
                else:
                    remain.append(tmp)
            maps = remain + maps
        ans +=1
        arr = save_arr
    print(ans)