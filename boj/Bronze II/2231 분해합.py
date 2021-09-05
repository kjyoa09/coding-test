n = int(input())

for i in range(1,n):
    if i + sum(map(int,str(i))) == n:
        print(i)
        break
else:
    print(0)
