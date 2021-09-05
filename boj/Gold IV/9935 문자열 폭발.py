## Index 로 풀었을 때에는 pypy로 통과... >> python 3으로는 안되네;;
## Slice 로는 시간초과..
## Del로 하면 더 빠르네;; 
## https://stackoverflow.com/questions/29193127/is-it-faster-to-truncate-a-list-by-making-it-equal-to-a-slice-or-by-using-del
## 일반적으로 Del로 지우는 것이 더 빠른듯...
import sys
sys.stdin = open("in.txt","r")
st = sys.stdin.readline().rstrip()
boom = list(sys.stdin.readline().rstrip())
Len = len(boom)
ans = []
for num in st:
    ans.append(num)

    if len(ans) >= Len and ans[-Len:] == boom:
        del ans[-Len:]
if len(ans) == 0:
    print("FRULA")
else:
    print(''.join(ans))    

'''
import sys
sys.stdin = open("in.txt","r")
st = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()
Len = len(boom)
ans = []
for num in range(len(st)):
    ans.append(st[num])
    if len(ans) < Len:
        continue
    else:
        tmp = ""
        for i in range(Len):
            tmp += ans.pop()
        if tmp[::-1] != boom:
            ans += list(tmp[::-1])
if len(ans) == 0:
    print("FRULA")
else:
    print(''.join(ans))    




while st:
    ans += st[0]
    st = st[1:]

    if ans[-Len:] == boom:
        ans = ans[:-Len]
        if len(ans) < Len:
            st = ans + st
            ans = ""
        else:
            st = ans[-Len:] + st
            ans = ans[:-Len]

if len(ans) == 0 :
    print("FRULA")
else:
    print(ans)
'''
'''
while len(st) != 0:
    tmp = st.find(boom)
    if tmp == -1 :
        break
    else:
        st = st.replace(boom,"")
if len(st) == 0:
    print("FRULA")
else:
    print(st)
'''