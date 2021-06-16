import sys
n,m = map(int,sys.stdin.readline().strip().split())

wf = []
bf = []
for i in range(4):
    wf += [["W","B"] * 4]
    wf += [["B","W"] * 4]
    bf += [["B","W"] * 4]
    bf += [["W","B"] * 4]

def check(arr):
    cnt1 = 0
    cnt2 = 0
    
    for i in range(8):
        cnt1 += sum([True for x,y in zip(arr[i],wf[i]) if x!=y])
        cnt2 += sum([True for x,y in zip(arr[i],bf[i]) if x!=y])

    return min(cnt1,cnt2)

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

ans = float("INF")

for r in range(0,n-7):
    for c in range(0,m-7):
        tmp = [arr[tr][c:c+8] for tr in range(r,r+8)]

        tmp = check(tmp)

        if tmp < ans:
            ans = tmp
print(ans)
