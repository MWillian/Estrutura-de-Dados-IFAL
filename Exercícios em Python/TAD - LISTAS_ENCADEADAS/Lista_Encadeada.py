from Noh import Noh

class ListaNaoOrdenada:
    def __init__(self):
        self.head = None
    
    def is_empty (self):
        return self.head == None

    def add_fim(self, item):
        temp = Noh(item)
        if self.head is None:
            self.head = temp
        else:
            atual = self.head
            while atual.getNext() is not None:
                atual = atual.getNext()
            atual.setNext(temp)

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
    
    def remove_first(self):
        if self.head is not None:
            self.head = self.head.getNext()
        else:
            "A Lista está vazia"
        
    def print_lista(self):
        atual = self.head
        print("Lista atual:")
        if atual is None:
            print("vazia")
        while atual is not None:
            print(atual.getData())
            atual = atual.getNext()

