n = int(input())
for i in range(n):
    tmp = list(map(int,input().split()))
    leng = tmp.pop(0)
    a = sum([1 for x in tmp if x > sum(tmp)/leng])/leng * 100
    print("%.3f"%(a) + "%")
