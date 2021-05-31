# 재귀함수
# 끝까지 가고 이후 계산 이게 Backtracking인가
import sys,math
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())

k = math.log(N//3,2)
ans =    ['  *   ',
           ' * *  ',
           '***** ']

def pp(k):
    global ans
    if k == 0:
        return
    else:
        pp(k-1)
        tmp = [x + x for x in ans]
        blank = " " * ((len(tmp[0]) - len(ans[-1]))//2)
        ans = [blank + x + blank for x in ans ] + tmp
pp(k)

for i in ans:
    print(i)