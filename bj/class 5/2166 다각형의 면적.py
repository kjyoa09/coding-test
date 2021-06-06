# https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D
# 신기하네;;
# 신발끈 공식... 모르면.. 못풀듯?

import sys
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
dot = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    dot.append((x,y))

a,b=0,0
for i in range(N):
    if i == N-1:
        a += dot[i][0] * dot[0][1]
        b -= dot[i][1] * dot[0][0]
    else :
        a += dot[i][0] * dot[i+1][1]
        b -= dot[i][1] * dot[i+1][0]
print(abs(a+b)/2)