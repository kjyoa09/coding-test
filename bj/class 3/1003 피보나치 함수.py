n = int(input())
dic = {0:[1,0],1:[0,1]}

for i in range(2,41):
    a,b = dic[i-1]
    c,d = dic[i-2]
    dic[i] = [a+c,b+d]

    
for i in range(n):
    tmp = int(input())
    for j in dic[tmp]:
        print(j,end = " ")
    print()
