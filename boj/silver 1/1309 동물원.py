# 추가된 칸 >> 모두 공백일 때, 앞칸 경우의 수 전부
#          >> 오, 앞칸 공백 or 앞칸 왼
#          >> 왼, 앞칸 공백 or 앞칸 오

N = int(input())
dp = [1,1,1] 
for i in range(N-1):
    dp = [sum(dp)%9901,(dp[0] + dp[1])%9901,(dp[0] + dp[2])%9901]
print(sum(dp)%9901)