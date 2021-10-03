from sys import stdin
input = stdin.readline

N = int(input())
num = list(list(map(int,input().strip().split(' '))))
sim = list(map(int,input().strip().split(' ')))
ans = []
def dfs(idx,sim,Num):
    global ans
    if idx == N:
        ans.append(Num)
    for ix,v in enumerate(sim):
        if v == 0:
            continue
        else:
            sim[ix] -= 1
            if ix == 0:
                dfs(idx+1,sim,Num+num[idx])
            if ix == 1:
                dfs(idx+1,sim,Num-num[idx])
            if ix == 2:
                dfs(idx+1,sim,Num*num[idx])
            if ix == 3:
                if Num < 0 :
                    Num *= -1
                    dfs(idx+1,sim,-1 *(Num//num[idx]))
                else:
                    dfs(idx+1,sim,(Num//num[idx]))
            sim[ix] += 1

dfs(1,sim,num[0])
print(max(ans))
print(min(ans))
