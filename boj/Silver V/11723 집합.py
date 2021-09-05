import sys
n = int(sys.stdin.readline())

s = set()

for i in range(n):

    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:
        if tmp[0] == "all":
            s = set(list(range(1,21)))
        else:
            s = set()
    else:
        if tmp[0] == "add":
            s = s | {int(tmp[1])}
        elif tmp[0] == "remove":
            s = s - {int(tmp[1])}
        elif tmp[0] == "check":

            if int(tmp[1]) in s:
                print(1)
            else: print(0)
        else:
            if int(tmp[1]) in s:
                s = s - {int(tmp[1])}
            else:
                s = s | {int(tmp[1])}