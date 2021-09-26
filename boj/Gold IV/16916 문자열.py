# re
from sys import stdin
import re
stdin = open('in.txt','r')
input = stdin.readline
A,B = input().strip(),input().strip()
print(0 if re.search(B,A) == None else 1)
