# Knapsack 알고리즘
# 무게 무거운 순으로 Sort >> K 만큼 ans 배열 생성
# ans 뒤에서 부터 물건을 넣었을 때 보다 ans가 작으면 바꿔줌
import sys
sys.stdin = open("in.txt","r")
N,K = map(int,sys.stdin.readline().rstrip().split()) #물건 수 : 한계
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
arr.sort(key = lambda x:-x[0]) #무게:가치
ans = [0] * (K + 1)

for W,V in arr:
    for idx in range(K,-1,-1):
        if idx - W >= 0 and ans[idx] < V + ans[idx - W]:
            ans[idx] = V + ans[idx - W]
print(ans[K])