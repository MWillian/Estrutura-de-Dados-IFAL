class Noh:
    def __init__(self,valor_inicial):
        self.valor = valor_inicial
        self.proximo = None
    
    def setNext(self,proximo):
        self.proximo = proximo
    
    def setData(self,dados):
        self.valor = dados
    
    def getNext(self):
        return self.proximo

    def getData(self):
        return self.valor