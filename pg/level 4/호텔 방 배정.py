# hashtable array도 이렇게 짜나 ..?
# Union & Find 
# dictionary로 구현 >> list면 K <= 10**12여서 힘들듯.. 

from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
class ftn:
    def __init__(self):
        self.dic = {}
    
    def find(self,idx):
        
        if self.dic.get(idx,0) == 0:
            return idx
        else:
            self.dic[idx] = self.find(self.dic[idx])
            return self.dic[idx]

def solution(k, room_number):
    sol = ftn()
    ans = []
    for num in room_number:
        if sol.dic.get(num,0) != 0:
            num = sol.find(num)
        ans.append(num)
        sol.dic[num] = num +1
    #print(sol.dic)
    return ans