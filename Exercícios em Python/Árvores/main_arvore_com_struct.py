# construção do tipo árvore
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp
    
    def getRightChild(self):
        return self.getRightChild

    def getLeftChild(self):
        return self.getLeftChild
    
    def setRootVal(self,newRoot):
        self.key = newRoot
    
    def getRootVal(self):
        return self.key
    
    def __repr__(self):
        L = self.leftChild
        R = self.rightChild
        return(f"[{self.key},[{L}],[{R}]]")
    
    