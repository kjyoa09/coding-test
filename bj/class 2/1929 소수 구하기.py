ch = [True] * 1000001
ch[1] = False

for i in range(2,1000000):
    if ch[i]:
        for n in range(i+i,1000000,i):
            ch[n] = False


s,e = map(int,input().split())

for i in ch[s:e+1]:
    if i:
        print(s)
    s += 1
