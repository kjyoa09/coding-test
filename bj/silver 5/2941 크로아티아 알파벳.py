s = list(input())
ans = 0

while s:
    tmp = s.pop(0)
    if tmp == "c":
        if len(s) > 0 and s[0] in ["-","="]:
            s.pop(0);ans +=1
        else:
            ans += 1
    elif tmp == "d":
        if len(s) > 0 and s[0] == "-":
            s.pop(0);ans += 1
        elif len(s) > 1 and s[:2] == ["z","="]:
            s = s[2:];ans += 1
        else:
            ans +=1
    elif tmp == "l":
        if len(s) > 0 and s[0] == "j":
            s.pop(0);ans += 1
        else:
            ans += 1

    elif tmp == "n":
        if len(s) > 0 and  s[0] == "j":
            s.pop(0);ans += 1
        else:
            ans += 1
      
    elif tmp == "s":
        if len(s) > 0 and  s[0] == "=":
            s.pop(0);ans += 1
        else:
            ans += 1
      
    elif tmp == "z":
        if len(s) > 0 and s[0] == "=":
            s.pop(0);ans += 1
        else:
            ans += 1
    else: ans += 1
print(ans)
