def solution(cookie):
    N = len(cookie)
    arr = [0]
    for n in range(N):
        arr.append(arr[-1] + cookie[n])

    ans = 0
    for s in range(N+1):
        for e in range(s,N+1):
            Sum = arr[e] - arr[s]
            tmp = Sum//2
            if tmp > ans and Sum%2 == 0:
                for tmid in range(s,e):
                    if arr[tmid] - arr[s] == tmp:
                        ans = tmp
                        break
    
    return ans