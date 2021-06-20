# 수정해야함
from sys import stdin
x1,y1,x2,y2 = map(int,stdin.readline().rstrip().split())
x3,y3,x4,y4 = map(int,stdin.readline().rstrip().split())

def ftn(q,w,e,r):
    a = (w-r)/(q-e)
    b = w-a*q 
    return a,b   

if (x1==x2 and y1==y2) and (x3==x4 and y3==y4) : # 둘 다 점
    if x1==x3 and y1==y4 :
        print(1)
    else:
        print(0) 

elif (x1==x2 and y1==y2) : # L1 만점
    if x3==x4:
        if x3==x1==x4 and min(y3,y4) <= y1 <= max(y3,y4):
            print(1)
        else:
            print(0)
    else:
        a,b = ftn(x3,y3,x4,y4)
        if min(y3,y4) <= a*x1+b <= max(y3,y4):
            print(1)
        else:
            print(0)

elif (x3==x4 and y3==y4) : # L2 만점
    if x1==x2:
        if x1==x2==x3 and min(y1,y2) <= y3 <= max(y1,y2):
            print(1)
        else:
            print(0)
    else:
        a,b = ftn(x1,y1,x2,y2)
        if min(y1,y2) <= a*x3+b <= max(y1,y2):
            print(1)
        else:
            print(0)
else:
    ccw1 = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    ccw2 = (x2-x1)*(y4-y1) - (y2-y1)*(x4-x1)

    ccw3 = (x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)
    ccw4 = (x4-x3)*(y2-y3) - (y4-y3)*(x2-x3)
    if ccw1*ccw2 <= 0 and ccw3*ccw4 <= 0:
        if ccw1*ccw2 == 0 and  ccw3*ccw4 == 0:
            if min(x1,x2) <= min(x3,x4) <= max(x1,x2)  and min(y1,y2) <= min(y3,y4) <= max(y1,y2):
                print(1)
            elif min(x3,x4) <= min(x1,x2) <= max(x3,x4)  and min(y3,y4) <= min(y1,y2) <= max(y3,y4):
                print(1)
            else :
                print(0)
        else:
            print(1)
    else:
        print(0)
