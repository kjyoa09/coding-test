import sys
ans = 0
for i in range(4):
    ans += int(input())
print(ans//60,ans%60,sep = "\n")
