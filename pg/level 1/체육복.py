def solution(n, lost, reserve):
    Lost = [x for x in lost if x not in reserve]
    Reserve = [x for x in reserve if x not in lost]
    
    Lost.sort()
    print(Lost)
    Reserve = set(Reserve)
    
    ans = 0

    for l in Lost[::-1]:
        print(l)
        if set([l + 1]) & Reserve:
            Reserve = Reserve - set([l + 1])
        elif set([l - 1]) & Reserve:
            Reserve = Reserve - set([l - 1])
        else: 
            ans +=1
    return n - ans