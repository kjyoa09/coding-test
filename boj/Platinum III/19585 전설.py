from sys import stdin,stdout
stdin = open('in.txt')
input = stdin.readline

from collections import defaultdict

class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        node = self.root

        for char in word:
            node = node.child[char]
        node.word = True

    def search(self,word,n):
        node = self.root

        for i in range(n):
            if word[i] not in node.child:
                return i if node.word else 0
            node = node.child[word[i]]

C, N = map(int, input().split())
c_trie = Trie()
n_trie = Trie()
for _ in range(C):
    c_trie.insert(input().rstrip())
for _ in range(N):
    n_trie.insert(input().rstrip()[::-1])

for _ in range(int(input())):
    query = input().rstrip()
    n = len(query)
    idx1 = c_trie.search(query,n)
    if not idx1:
        print('No')
        continue
    idx2 = n_trie.search(query[::-1], n)
    print('Yes'if idx1+idx2==n else 'No')

'''color_dic = {}
C,N = map(int,input().strip().split(' '))
c = {}
for _ in range(C):
    cur_dic = color_dic
    for c in input().strip():
        if c not in cur_dic:
            cur_dic[c] = {}
        cur_dic = cur_dic[c]
    cur_dic['data'] = True

team_dic = {}

for _ in range(N):
    cur_dic = team_dic
    for n in input().strip():
        if n not in cur_dic:
            cur_dic[n] = {}
        cur_dic = cur_dic[n]
    cur_dic['data'] = True

for _ in range(int(input())):
    tmp = input().strip()
    Len = len(tmp)
    cur_dic = color_dic
    for idx in range(Len):
        if tmp[idx] in cur_dic:
            cur_dic = cur_dic[tmp[idx]]
        else:
            if cur_dic.get('data',0) and tmp[idx] in team_dic:
                cur_dic = team_dic[tmp[idx]]            
            else:
                stdout.write('No\n')
                break
    else:
        if cur_dic.get('data',0):
            stdout.write('Yes\n')
        else:
            stdout.write('No\n')'''