dp = [0,1,3]
for i in range(250):
    dp += [dp[-1] + dp[-2] * 2]
while 1:
    try :
        print(dp[int(input())])
    except:
        break