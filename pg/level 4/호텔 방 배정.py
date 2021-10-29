# hashtable array도 이렇게 짜나 ..?

from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
class ftn:
    def __init__(self):
        self.dic = {}
    
    def find(self,idx):
        
        if self.dic.get(idx,0) == 0:
            return idx
        else:
            tmp = self.find(self.dic[idx])
            self.dic[idx] = tmp
            return tmp
        
        # while 1:            
        #     if self.dic.get(idx,0) == 0:
        #         return idx
        #     else:
        #         idx = self.dic[idx]

def solution(k, room_number):
    sol = ftn()
    ans = []
    
    for num in room_number:
        if sol.dic.get(num,0) == 0:
            ans.append(num)
            sol.dic[num] = num + 1
        else:
            sol.find(num)
            tmp = sol.dic[num]
            ans.append(tmp)
            sol.dic[tmp] = tmp + 1

    return ans