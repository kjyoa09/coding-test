_ = int(input())
arr = list(map(int,input().split()))

m = max(arr)

arr = [x/m*100 for x in arr]

print(sum(arr)/len(arr))
