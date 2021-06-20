ans = [0,10]
s = [1,1,1,1,1,1,1,1,1,1]
mul = [10,9,8,7,6,5,4,3,2,1]
for i in range(64):
    ans += [sum([x*y for x,y in zip(s,mul)])]
    tmp = [s[0]]
    for i in range(1,10):
        tmp += [tmp[-1] + s[i]]
    s = tmp

from sys import stdin
stdin = open("in.txt")
T = int(stdin.readline())
for _ in range(T):
    print(ans[int(stdin.readline())])
print(ans[1])