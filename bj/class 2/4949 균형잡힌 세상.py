import sys

def ch(ls):
    s = []
    m = []
    idx = 0
    while ls:
        tmp = ls.pop(0)
        idx += 1
        
        if tmp == "(":
            s += [idx]
        elif tmp == "[":
            m += [idx]

        elif tmp == ")":
            if len(s) == 0:
                return False
            elif len(m) == 0 or s[-1] > m[-1]:
                s.pop()
            else:

                return False

        elif tmp == "]":
            if len(m) == 0:
                return False
            elif len(s) == 0 or m[-1] > s[-1]:
                m.pop()
            else:
                return False
        
    if len(s) == len(m) == 0:
        return True
    else:
        return False

while 1:
    a = sys.stdin.readline().rstrip()
    if a == ".":
        break

    a = [x for x in list(a) if ord(x) in [ord(")"),ord("("),ord("["),ord("]")]]

    if ch(a):
        print("yes")
    else:
        print("no")






