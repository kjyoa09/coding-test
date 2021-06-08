a,b = input().split()
a,b = map(int,[a[::-1],b[::-1]])
print(max(a,b))
