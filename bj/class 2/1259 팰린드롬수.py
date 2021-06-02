import sys

while 1:
    tmp = sys.stdin.readline().strip()
    
    if tmp == "0":
        break
    else:
        if tmp == tmp[::-1]:
            print("yes")
        else:
            print("no")
