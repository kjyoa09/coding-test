# 수학 문제 : 등차수열 
import sys
sys.stdin = open("in.txt","r")
T = int(sys.stdin.readline())

for _ in range(T):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    length = y - x
    i = 0
    while 1:
        if i * (i + 1)/2 + i * (i-1)/2 > length:
            i -= 1
            break
        else :i += 1
    tmp = i * (i + 1)//2 + i * (i-1)//2
    if length - tmp == 0:
        print(i + i-1 )
    elif length - tmp <= i:
        print(i + i)
    else:
        print(i + i +1)
    
'''
    print(length)

0 : 0
1 : 1
2 : 1 1
3 : 1 1 1
4 : 1 2 1
5 : 1 2 1 1
6 : 1 2 2 1
7 : 1 2 2 1 1
8 : 1 2 2 2 1
9 : 1 2 3 2 1
'''

