from sys import stdin
stdin = open('in.txt')
input = stdin.readline
N,M,K = map(int,input().strip().split(' '))
card = {idx:k for idx,k in enumerate(sorted(map(int,input().strip().split(' '))))}
arr  = list(map(int,input().strip().split(' ')))


def find(lt,rt,num,card):
    ans = 4_000_001
    
    while lt<=rt:
        mid = (lt+rt)//2
        if card[mid] <= num:
            lt = mid + 1
        else:
            if ans > card[mid]:
                ans = card[mid]
                idx = mid
            rt = mid - 1
    return idx

for num in arr:
    idx = find(0,M-1,num,card)
    print(card[idx])
    del card[idx]
    M -=1 