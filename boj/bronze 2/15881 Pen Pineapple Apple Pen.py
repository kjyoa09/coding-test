import sys
sys.stdin = open("in.txt")
sys.stdin.readline()
string = sys.stdin.readline().rstrip()

patt = "pPAp"

n = 0
ans = 0

for idx,i in enumerate(string):
    if i == patt[n]:
        if n == 3:
            ans += 1
            n = 0
        else:
            n+=1
    else:
        if i == "p":
            n = 1
        else:
            n = 0
print(ans)

