from main_arvore_com_struct import *

def constroi_Arvore(raiz):
    arvore = BinaryTree(raiz)
    arvore.insertLeft('d')
    arvore.insertLeft('b')
    arvore.insertRight('f')
    arvore.insertRight('e')
    arvore.insertLeft('c')
    return arvore

print(constroi_Arvore('a'))

