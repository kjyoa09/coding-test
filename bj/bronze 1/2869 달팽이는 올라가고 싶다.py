import sys
a,b,v = map(int,sys.stdin.readline().split())

ans,tmp = divmod(v-a,a-b)

if tmp == 0 :
    print(ans +1)
else:
    print(ans +2)

