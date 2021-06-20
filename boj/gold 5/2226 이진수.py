ans = [0,1]
for i in range(2,int(input())+1):
    if i%2 == 1:
        ans = [ans[0] + ans[1] - 1,ans[0] + ans[1]]
    else:
        ans = [ans[0] + ans[1],ans[0] + ans[1]]
print(ans[0])
