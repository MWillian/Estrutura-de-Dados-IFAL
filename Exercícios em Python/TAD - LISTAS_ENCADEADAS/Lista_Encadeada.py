from Noh import *

class ListaNaoOrdenada:
    def __init__(self):
        self.head = None
    
    def is_empty (self):
        return self.head == None

    def add (self,item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size (self):
        atual = self.head
        contador = 0
        while atual != None:
            contador += 1
            atual = atual.getNext()
        return contador
    
    def search (self,item):
        atual = self.head
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                atual = atual.getNext()
        return encontrou
    
