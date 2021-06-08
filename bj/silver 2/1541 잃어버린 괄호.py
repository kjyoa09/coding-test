import sys; 
import re

arr = sys.stdin.readline().strip()

sim = re.findall("[0-9]*(-|\+)[0-9]*",arr)
num = re.findall("([0-9]+)[-|\+]*",arr)

ans = int(num.pop(0))

while sim:
    tmp = sim.pop(0)

    if tmp == "+":
        b = num.pop(0)
        ans += int(b)
    else:
        v = int(num.pop(0))
        if len(sim) > 0 and sim[0] == "+":
            while sim and sim[0] == "+" :
                v += int(num.pop(0))
                sim.pop(0)
        ans -= v
print(ans)
