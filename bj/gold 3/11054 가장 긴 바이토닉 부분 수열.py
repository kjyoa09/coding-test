# dp 두번 :
import sys
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

dp_as = [(0,0)]
dp_de = [[0,0]]
for as_num in arr:
    as_cnt = -1
    for x,cnt in dp_as:
        if x < as_num and as_cnt < cnt:
            as_cnt = cnt
    dp_as.append((as_num,as_cnt + 1))

for de_num in arr[::-1]:
    de_cnt = -1
    for x,cnt in dp_de:
        if x < de_num and de_cnt < cnt:
            de_cnt = cnt
    dp_de.append((de_num,de_cnt + 1))

print(max([x[1]+y[1] for x,y in zip(dp_as[1:],dp_de[::-1][:-1])])-1)
