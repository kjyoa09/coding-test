from sys import stdin
stdin = open("in.txt")
input = stdin.readline
N = int(input())
maps = [list(map(int,input().rstrip().split())) for _ in range(N)]
W1,W2,B1,B2 = [True] * (2*N-1),[True] * (2*N-1),[True] * (2*N-1),[True] * (2*N-1)
arr = [[0,2,4,6,8,10],[1,3,5,7,9,11]]
ans = [-1,-1]

def dfs(r,c,d1,d2,num,idx,li):#row,col,diag1,diag2,WB,col_arr
    global ans
    if r == N:
        if ans[idx] < num:
            ans[idx] = num
    else:
        if maps[r][arr[li][c]] and d1[r+arr[li][c]] and d2[r-arr[li][c]+(N-1)]:
            d1[r+arr[li][c]],d2[r-arr[li][c]+(N-1)] = False,False
            if 0<=arr[li][c+1]<N:
                dfs(r,c+1,d1,d2,num+1,idx,li)
            else:
                if li:
                    dfs(r+1,0,d1,d2,num+1,idx,0)
                else:
                    dfs(r+1,0,d1,d2,num+1,idx,1)
            d1[r+arr[li][c]],d2[r-arr[li][c]+(N-1)] = True,True
        if 0<=arr[li][c+1]<N:
            dfs(r,c+1,d1,d2,num,idx,li)
        else:
            if li :
                dfs(r+1,0,d1,d2,num,idx,0)
            else:
                dfs(r+1,0,d1,d2,num,idx,1)
dfs(0,0,W1,W2,0,0,0)
dfs(0,0,B1,B2,0,1,1)
print(sum(ans))
