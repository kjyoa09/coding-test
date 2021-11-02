# Np,Pp,Qp : 현재,늘릴 구간, 줄일 구간
# 

from collections import Counter
def solution(land, P, Q):
    dic = Counter([y for x in land for y in x])
    keys = sorted(dic.keys())
    re = float('inf')
    for idx,key in enumerate(keys):

        if idx == 0:
            ans,Pp,Qp = 0,0,0

            for k,v in dic.items():

                if k == key:
                    Np = v

                else:
                    ans += (k-key) * v * Q 
                    Qp += v

        else:
            Pp += Np
            Np = dic[key]
            Qp -= dic[key]

            ans += (keys[idx-1]-key) * Np * Q
            ans -= (keys[idx-1]-key) * Pp * P
            ans += (keys[idx-1]-key) * Qp * Q

        if ans < re:
            re = ans

    return re