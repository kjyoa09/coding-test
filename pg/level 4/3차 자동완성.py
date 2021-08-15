'''
Node dic에 미리 알파벳 넣어두면 시간초과나옴;;
'''
class Node:
    def __init__(self):
        self.cnt = 0
        self.dic = {}
        
class ftn:
    def __init__(self):
        self.tree = Node()
        self.ans = 0
        
    def insert(self,word):
        cur_tree = self.tree
        
        for w in word:
            if w not in cur_tree.dic:
                cur_tree.dic[w] = Node()
            cur_tree = cur_tree.dic[w]
            cur_tree.cnt += 1

    def find(self,word):
        cur_tree = self.tree
        
        for idx,w in enumerate(word):
            cur_tree = cur_tree.dic[w]
            if cur_tree.cnt == 1:
                break
        
        self.ans += idx + 1
        
def solution(words):
    
    sol = ftn()
    
    for word in words:
        sol.insert(word)
    

    for word in words:
        sol.find(word)

    return sol.ans
