class Node:
    def __init__(self):
        self.cnt = 0
        self.dic = {}

class ftn:
    def __init__(self):
        self.tree = Node()
        self.inv = Node()
        
    def insert(self,word):
        cur_tree = self.tree
        if len(word) not in cur_tree.dic:
            cur_tree.dic[len(word)] = Node()
        cur_tree = cur_tree.dic[len(word)]
        cur_tree.cnt += 1
        
        for w in word:
            if w not in cur_tree.dic:
                cur_tree.dic[w] = Node()
            cur_tree = cur_tree.dic[w]
            cur_tree.cnt += 1
            
        cur_tree = self.inv
        if len(word) not in cur_tree.dic:
            cur_tree.dic[len(word)] = Node()
        cur_tree = cur_tree.dic[len(word)]
        cur_tree.cnt += 1
        
        for w in word[::-1]:
            if w not in cur_tree.dic:
                cur_tree.dic[w] = Node()
            cur_tree = cur_tree.dic[w]
            cur_tree.cnt += 1
    
    def count(self,query):
        Len = len(query)
        if query[0] == "?":
            cur_tree = self.inv
            query = query[::-1]        
        else:
            cur_tree = self.tree

        if Len not in cur_tree.dic:
            return 0
        else:
            cur_tree = cur_tree.dic[Len]
            
            if query[0] == query[-1] == "?":
                return cur_tree.cnt
            
            else:
                for q in query:
                    if q == "?":
                        return cur_tree.cnt
                    
                    elif q not in cur_tree.dic:
                        return 0
                    
                    else:
                        cur_tree = cur_tree.dic[q]


def solution(words, queries):
    sol = ftn()
    ans = []
    
    for word in words:
        sol.insert(word)

    for query in queries:
        ans.append(sol.count(query))
    
    return ans