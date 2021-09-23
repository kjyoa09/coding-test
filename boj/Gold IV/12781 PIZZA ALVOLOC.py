# 선분 교차 판정
# ccw == 0 제외
def ccw(x1,y1,x2,y2,x3,y3):
    tmp= (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    if tmp> 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

def connect(x1,y1,x2,y2,x3,y3,x4,y4):
    answer=0
    didanswer=False


    if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)<0 and ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)<0:
        if not didanswer:
            answer=1
    return answer


from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline
x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().strip().split(' '))

print(connect(x1,y1,x2,y2,x3,y3,x4,y4))