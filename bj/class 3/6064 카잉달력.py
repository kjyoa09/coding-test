#하나 고정 후에 다른 하나 더해가며 RES 구함 RES 중복 값 나오면 Break 
import sys
sys.stdin = open("in.txt","r")
T = int(sys.stdin.readline())

for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().rstrip().split())
    s = x
    res = [True] * (N + 1)
    while 1:
        tmp = s % N
        if tmp == 0:
            tmp = N
        if tmp == y:
            print(s)
            break
        else:
            if res[tmp]:
                res[tmp] = False
                s += M
            else:
                print(-1)
                break
