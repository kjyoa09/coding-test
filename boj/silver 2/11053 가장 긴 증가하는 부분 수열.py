# Knapsack으로 풀려고 했는데...  적용하기가 애매한 것 같음 [가방 무게 같은 제한이 없어서] 
# 그냥 자신이 낄 수 있는 수열[가장 뒷 값이 자신보다 작은 수열]에서 가장 긴 수열에 넣는 식으로 dp
import sys
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
ans = [[0,0]]

for i in arr:
    re = [-1,-1]
    for tmp in ans[::-1]:
        if tmp[1] < i and tmp[0] + 1 > re[0]:
            re = [tmp[0]+1,i]
    if re == [-1,-1]:
        re = [0,i]
    ans.append(re)
ans.sort(key=lambda x:-x[0])
print(ans[0][0])
