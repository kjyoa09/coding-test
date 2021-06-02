from collections import Counter

dic = Counter(input().upper())

m = max(dic.values())

ans = ""

for k,v in dic.items():
    if v == m:
        if ans == "":
            ans = k
        else:
            print("?")
            break
else:
    print(ans)
