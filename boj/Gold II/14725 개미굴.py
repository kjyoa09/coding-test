from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    arr = input().strip().split(' ')
    curdic = dic
    for st in arr[1:]:
        if st not  in curdic:
            curdic[st] = {}
        curdic = curdic[st]

def dfs(dic,num):
    key = sorted(dic.keys())
    for k in key:
        print("--"*num,k,sep = '')
        dfs(dic[k],num+1)
dfs(dic,0)