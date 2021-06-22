from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
L,C = map(int,input().rstrip().split())
arr = input().rstrip().split()
arr.sort()
mo = [False] * 26
for ch in ["a","e","i","o","u"]:
    mo[ord(ch)-97] = True
ja = [True if mo[i] == False else False for i in range(26)]

def dfs(idx,poss):
    if len(poss) == L:
        if sum([mo[ord(x)-97] for x in poss]) >= 1 and sum([ja[ord(x)-97] for x in poss]) >=2:
            print("".join(poss))
    elif idx >= C:
        return
    else:
        for ii,ch in enumerate(arr[idx:]):
            dfs(idx+ii+1,poss +[ch])
dfs(0,[])
