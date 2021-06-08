import sys
n,l = map(int,sys.stdin.readline().split())
maps = []
def check(tmp):
    ch = [0] * n
    for i in range(n):
        if i == 0:
            now = tmp[i]
            continue
        next_ = tmp[i]
        if next_ == now:
            continue
        elif abs(next_ - now) > 1:
            return False
        else:
            if next_ < now:
                if i + l <= n and all(x == next_ for x in tmp[i:i+l]):
                    ch = [ch[x] + 1 if i <= x <i + l else ch[x] for x in range(n)]
                else:
                    return False
            else:
                if i - l >= 0 and all(x == now for x in tmp[i-l:i]):
                    ch = [ch[x] + 1 if i-l <= x <i  else ch[x] for x in range(n)]
                else: return False
        now = next_
   
    if all(x < 2 for x in ch):
        return True
    else:
        return False
for _ in range(n):
    maps += [list(map(int,sys.stdin.readline().split()))]
ans =  0
for i in maps:
    ans += check(i)
maps = list(map(list,zip(*maps)))
for i in maps:
    ans += check(i)
print(ans)

