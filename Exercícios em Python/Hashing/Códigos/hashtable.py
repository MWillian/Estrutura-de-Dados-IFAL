class HashTable:
    def __init__(self):
        self.tamanho = 11
        self.slots = [None]*self.tamanho
        self.valores = None*self.tamanho
    
    def hashfunction(self,chave,tamanho):
        return chave % tamanho

    def rehash(self,oldhash,tamanho):
        return (oldhash + 1) % tamanho
    
    def put(self,chave,valor):
        valorHash = self.hashfunction(chave,len(self.slots))

        if self.slots[valorHash] == None:
            self.slots[valorHash] = chave
            self.valores[valorHash] = valor

