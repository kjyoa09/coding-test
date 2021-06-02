#입력의 마지막에는 0 두 개가 들어온다.
while 1:
    a,b = map(int,input().split())
    if a==b==0:
        break
    else:
        print(a+b)