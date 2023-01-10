import sys
sys.stdin = open('in.txt')
input = sys.stdin.readline

arr = [[0] * 2 for _ in range(21)]

arr[1] = [1,1]

for i in range(2,len(arr)):
    a,b = arr[i-1] # 탄생, 전체
    pa = b
    pb = b + pa
    pb -= arr[i-3][0] if i-3 > -1 and (i-3)%2 == 1 else 0
    pb -= arr[i-4][0] if i-4 > -1 and (i-4)%2 == 0 else 0
    arr[i] = [pa,pb]
    
print(arr[int(input())][1])