# Index를 지정할 때에는 확실한 값에 의해 계산되게 지정
# post : l + r + node
# inner : l + node + r
import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("in.txt","r")
n = int(sys.stdin.readline())

innn = list(map(int,sys.stdin.readline().rstrip().split()))
post = list(map(int,sys.stdin.readline().rstrip().split()))

dic = {v:idx for idx,v in enumerate(innn)}

def dfs(in_s,in_e,po_s,po_e):
    if in_s > in_e or po_s > po_e:
        return
    # print(po_e,post[po_e])
    idx = dic[post[po_e]]
    print(innn[idx],end = " ")

    dfs(in_s,in_s + idx - 1, po_s,po_s + idx - in_s - 1)
    dfs(idx + 1,in_e,po_s + idx - in_s, po_e-1)    

dfs(0,n-1,0,n-1)

'''
def dfs(ino,po):
    if len(ino)==1:
        return print(ino[0],end = " ")
    else:

        idx = ino.index(po[-1])
        ino1 = ino[:idx]
        ino2 = ino[idx + 1:]
        
        po1 = po[:idx]
        po2 = po[idx:-1]
        
        print(ino[idx],end = " ")

        if len(ino1) != 0:
            dfs(ino1,po1)
        if len(ino2) != 0:
            dfs(ino2,po2)

dfs(inorder,postoder)
'''
