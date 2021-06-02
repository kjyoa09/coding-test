import sys
dic = {chr(i):i-96 for i in range(97,97+26)}

n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip())
mod = 1234567891
ans = 0
for idx,x in enumerate(arr):
    ans += dic[x]*31**idx
print(ans%mod)
