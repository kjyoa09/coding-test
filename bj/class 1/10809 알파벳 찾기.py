dic = {chr(k):-1 for k in range(97,122+1)}

s = input()

for idx,i in enumerate(s):
    if dic[i] == -1:
        dic[i] = idx
for v in dic.values():
    print(v,end = " ")

