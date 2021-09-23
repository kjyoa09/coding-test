def ccw(x1,y1,x2,y2,x3,y3):
    tmp= (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    if tmp> 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

from sys import stdin
stdin = open('in.txt')
input = stdin.readline

(x1,y1),(x2,y2),(x3,y3) = map(int,input().strip().split(' ')),map(int,input().strip().split(' ')),map(int,input().strip().split(' '))
print(ccw(x1,y1,x2,y2,x3,y3))