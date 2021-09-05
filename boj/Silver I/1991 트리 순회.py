import sys

sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())



class tree:
    def __init__(self,i,l,r):
        self.index = i
        self.left = l
        self.right = r
    
    def addNode(self,i,l,r):
        if self.index == i or self.index == None:
            self.index = i

            if l == ".":
                self.left = None
            else:
                self.left = tree(l,None,None)

            if r == ".":
                self.right = None
            else:
                self.right = tree(r,None,None)
            return True
        
        else:
            if self.left != None:
                flag = self.left.addNode(i,l,r)
            
            else:
                flag = False
            
            if flag == True:
                return True
            else:
                if self.right != None:
                    flag = self.right.addNode(i,l,r)
                else:
                    flag = False


    def order(self,node,path):
        r = []
        l = []
        if node.left != None:
            l = self.order(node.left,path)
        if node.right != None:
            r = self.order(node.right,path)
        if path == -1:
            return [node.index] + l + r
        elif path == 0:
            return l + [node.index] + r
        else:
            return l + r + [node.index]
Tree = tree(None,None,None)
for _ in range(N):
    a,b,c = sys.stdin.readline().rstrip().split()
    Tree.addNode(a,b,c)

print("".join(Tree.order(Tree,-1)))
print("".join(Tree.order(Tree,0)))
print("".join(Tree.order(Tree,1)))