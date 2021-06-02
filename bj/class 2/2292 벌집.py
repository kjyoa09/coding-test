import sys

#sys.stdin = open("in1.txt")


k = int(sys.stdin.readline())
if k == 1:
    print(1)
else:
    k= k - 1
    cnt = 0
    while k > 0:
        k -= cnt * 6
        cnt += 1
    print(cnt)

    
    
