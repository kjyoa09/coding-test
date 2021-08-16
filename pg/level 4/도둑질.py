'''
DP
idx 0인집 털면 마지막 집 못텀
>> 0 부터 시작, 1부터 시작 
>> max 값 비교
'''
def solution(money):
    a,b = 0,money[0]
    for mo in money[1:-1]:
        a,b = max(a,b),a+mo
    c,d = 0,money[1]
    for mo in money[2:]:
        c,d = max(c,d), c+mo
    return max(a,b,c,d)