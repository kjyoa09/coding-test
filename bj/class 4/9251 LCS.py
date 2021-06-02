#알고리즘 
#LCS[i - 1][j]와 LCS[i][j - 1]: 현재의 문자를 비교하는 과정 이전의 최대 공통 부분수열은 계속해서 유지
import sys
sys.stdin = open("in.txt")
s = [sys.stdin.readline().strip(),sys.stdin.readline().strip()]
s.sort(key = lambda x:len(x))
sh = s[0];lo = s[1]
maps = [[0]*(len(sh)+1) for _ in range(len(lo)+1)]
for ss in range(1,len(sh)+1):
    for ll in range(1,len(lo)+1):
        if sh[ss-1] == lo[ll-1]:
            maps[ll][ss] = maps[ll-1][ss-1]+1
        else:
            maps[ll][ss] = max(maps[ll-1][ss],maps[ll][ss-1])
print(maps[-1][-1])


