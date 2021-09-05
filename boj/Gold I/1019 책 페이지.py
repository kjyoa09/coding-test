from sys import stdin
stdin = open("in.txt")
N = int(stdin.readline())
counts = [0] * 10
weight = 1
for step in range(len(str(N))):
    replaced = int(str(N // 10) + "9")
    remaining = replaced - N
    for i in range(len(counts)): counts[i] += (N // 10 + 1) * weight
    for i in range(10-remaining, 10): counts[i] -= weight
    for number in list(str(N)[:-1]):
        number = int(number)
        counts[number] -= remaining * weight
    counts[0] -= weight
    N //= 10
    weight *= 10
print(' '.join(map(str, counts)))