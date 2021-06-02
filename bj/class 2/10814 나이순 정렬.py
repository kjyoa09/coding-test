import sys


n = int(input())
ans = []
for idx,_ in enumerate(range(n)):
    a,b = sys.stdin.readline().split()
    ans += [(int(a),b,idx)]
ans.sort(key = lambda x:(x[0],x[2]))

for i in ans:
    print(i[0],i[1],sep =" ")
