# 구현
# 재귀함수를 통해 move 계산

from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

R,C,M = map(int,input().split(' '))

dic = {c:{} for c in range(1,C+1)}
ans = 0

def move(r,c,s,d,z,re):
    if d == 1: #up
        if r-re > 0:
            return r-re,c,s,d,z
        else:
            return move(1,c,s,2,z,re-(r-1))
    elif d == 2: #down
        if r + re <= R:
            return r+re,c,s,d,z
        else:
            return move(R,c,s,1,z,re-(R-r))
    
    elif d == 3: #right
        if c + re <= C:
            return r,c+re,s,d,z
        else:
            return move(r,C,s,4,z,re-(C-c))
    
    else: # left
        if c - re > 0:
            return r,c-re,s,d,z
        else:
            return move(r,1,s,3,z,re-(c-1))


for _ in range(M):
    r,c,s,d,z = map(int,input().split(' '))
    dic[c][r] = (r,c,s,d,z)

for c in range(1,C +1):
    if any(dic[c].values()):
        r = min(k for k,v in dic[c].items() if v )
        ans += dic[c][r][-1]
        del dic[c][r]
    
    tmp = {aa:{} for aa in range(1,C+1)}

    for cc in range(1,C+1):
        for rr in range(1,R+1):
            if dic[cc].get(rr,0):
                pr,pc,ps,pd,pz = dic[cc][rr]
                pr,pc,ps,pd,pz = move(pr,pc,ps,pd,pz,ps)

                if tmp[pc].get(pr,0):
                    if tmp[pc][pr][-1] < pz:
                        tmp[pc][pr] = (pr,pc,ps,pd,pz)
                else:
                    tmp[pc][pr] = (pr,pc,ps,pd,pz) 
    dic = tmp
print(ans)