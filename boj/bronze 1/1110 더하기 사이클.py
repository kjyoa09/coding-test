num = input()
Tmp = num
fun = lambda x:int(x[0]) + int(x[1])
cnt = 0
while 1:
    if len(Tmp) == 1:
        Tmp = "0" + Tmp
    
    Tmp = str(int(Tmp[-1] + str(fun(Tmp))[-1]))
    cnt += 1
    if Tmp == num:
        break
print(cnt)