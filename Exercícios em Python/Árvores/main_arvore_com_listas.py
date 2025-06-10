#CONSTRUINDO UMA ÁRVORE BINÁRIA:

#criação da classe árvore utilizando listas
def BinaryTree (r):
    return [r,[],[]]

# inserindo um nó a esquerda de uma árvore ou subárvore
def insertLeft(root,newBranch):
    t = root[1]
    if len(t) > 1:
        root[1] = [newBranch,t,[]]
    else:
        root[1] = [newBranch,[],[]]
    return root

# inserindo um nó a direita de uma árvore ou subárvore
def insertRight (root,newBranch):
    t = root[2]
    if len (t) > 1:
        root[2] = [newBranch,[],t]
    else:
        root[2] = [newBranch,[],[]]
    return root

#FUNÇÕES AUXILIARES: 

# retornando o valor da raiz da árvore
def getRootVal(root):
    return root[0]

# definindo um novo valor para a raiz 
def setRootVal(root,newVal):
    root[0] = newVal

# retornando o filho da esquerda, dada uma raiz
def getLeftChild (roo):
    return roo[1]

# retornando o filho da direita, dada uma raiz
def getRightChild (roo):
    return roo[2]


