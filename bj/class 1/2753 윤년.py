#윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
a = int(input())

if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
    print(1)
else:print(0)