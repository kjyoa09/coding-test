# 전위 순회한 결과 >> 후위 순회로 변환. 
# lt < node < rt
# 전위 node + lt + rt
# 후위 lt + rt + node
# 트리 만들어서 후위로 변경 >> 시간초과
# 분할 정복 사용

import sys
sys.stdin = open('in.txt',"r")
number = []

while 1:
    try :
        tmp = int(sys.stdin.readline())
        number.append(tmp)
    except :
        break

def dfs(start,end):
    if start > end:
        return
    else:
        node = number[start]
        lt = start +1
        while lt <= end:
            if number[lt] > node:
                break
            lt +=1
        dfs(start + 1,lt-1)
        dfs(lt,end)
        print(node)
dfs(0,len(number) - 1)

'''
import sys
sys.stdin = open('in.txt',"r")
sys.setrecursionlimit(20_000)
class Node:
    def __init__(self) :
        self.index = None
        self.right = None
        self.left  = None

class Tree:
    def __init__(self):
        self.root = None
    def addTree(self,V):
        if self.root == None:
            self.root = Node()
            curr_node = self.root
            curr_node.index = V
        else:
            curr_node = self.root
            while 1:
                if V < curr_node.index:
                    if curr_node.left == None:
                        curr_node.left = Node()
                        # print("Node",curr_node.index)
                        curr_node = curr_node.left
                        curr_node.index = V
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if curr_node.right == None:
                        curr_node.right = Node()
                        # print("Node",curr_node.index)
                        curr_node = curr_node.right
                        curr_node.index = V
                        break
                    else:
                        curr_node = curr_node.right
    def order(self,root):
        l = r = []
        if root.left != None:
            l = self.order(root.left)
        if root.right != None:
            r = self.order(root.right)
        print(root.index)
tree = Tree()

while 1:
    try :
        tmp = int(sys.stdin.readline())
    except :
        break
    tree.addTree(tmp)

tree.order(tree.root)
'''