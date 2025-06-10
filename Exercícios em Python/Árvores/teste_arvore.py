from main_arvore_com_listas import *

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
insertRight(getRightChild(r),5)

print(r)

def constroi_arvore(root):
    a = BinaryTree(root)
    insertLeft(a,'b')
    insertRight(getLeftChild(a),'d')
    insertRight(a,'c')
    insertLeft(getRightChild(a),'e')
    insertRight(getRightChild(a),'f')

