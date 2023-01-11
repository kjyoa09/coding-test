import sys

sys.stdin = open('in.txt')
input = sys.stdin.readline

n,k = map(int,input().strip().split(' '))
arr = list(map(int,input().strip().split(' ')))

t,s,ans = k,0,-float('inf')

for idx,v in enumerate(arr):
    if t:
        t-=1
    else:
        s-=arr[idx-k]
    s+=v    
    if t == 0:
        ans = max(ans,s)
print(ans)    