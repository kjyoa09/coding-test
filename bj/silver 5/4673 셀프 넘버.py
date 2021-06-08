ch = [True] * 10000
for v in range(1,10001):
    tmp = sum(map(int,str(v))) + v
    if tmp - 1 < 10000:
        ch[tmp - 1] = False
for idx,v in enumerate(ch):
    if v:
        print(idx+1)
