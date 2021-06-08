n = int(input())

for i in range(n):
    a,tmp = input().split()
    for j in tmp:
        print(j*int(a),end = "")
    print()
        
