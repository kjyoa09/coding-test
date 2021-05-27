# DP
# Cnt + C Cnt + V할 때 변수 잘 확인
import sys
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
for num in range(N):
    if num == 0:
        start_max = list(map(int,sys.stdin.readline().rstrip().split()))
        start_min = start_max[:]
    else:
        tmp = list(map(int,sys.stdin.readline().rstrip().split()))
        TMP_min = []
        TMP_max = []
        for i in range(3):
            if i == 0:
                TMP_max.append(max(start_max[0],start_max[1]) + tmp[0])
                TMP_min.append(min(start_min[0],start_min[1]) + tmp[0])
            elif i == 1:
                TMP_max.append(max(start_max) + tmp[1])
                TMP_min.append(min(start_min) + tmp[1])
            else:
                TMP_max.append(max(start_max[2],start_max[1]) + tmp[2])
                TMP_min.append(min(start_min[2],start_min[1]) + tmp[2])          
        start_max = TMP_max
        start_min = TMP_min

print(max(start_max),min(start_min),sep = " ")