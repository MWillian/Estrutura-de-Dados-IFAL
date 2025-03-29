class PilhaVazia(Exception):
    pass

class PilhaArray():
    def __init__(self, QUANTIDADE_MAX = None):
        self.pilha = []
        self.MAX_TAMANHO = QUANTIDADE_MAX
       
    def __len__(self):
        return len(self.pilha)
       
    def __size__(self):
        return self.__len__()
       
    def __isEmpty__(self):
        return len(self.pilha == 0)
       
    def __isFull__(self):
        if self.__len__() == self.MAX_TAMANHO and self.MAX_TAMANHO is not None:
            return True
        return False

    def __push__(self,valor):
        if self.__isFull__():
            raise ValueError("A pilha está cheia") 
        self.pilha.append(valor)

       
    def __top__(self):
        if self.__isEmpty__():
            raise PilhaVazia('A pilha está vazia')
        return self.pilha[-1]
       
    def __pop__(self):
        if self.__isEmpty__():
            raise PilhaVazia('A pilha está vazia')
        return self.pilha.pop()
       
    def inverte_texto(texto):
        pilha = PilhaArray()
        for letra in texto:
            pilha.__push__(letra)
            palavra = ""
        while not pilha.__isEmpty__():
            palavra += pilha.__pop__()
        return palavra
    def __copiaPilha__(p,q):
        temp = PilhaArray()
        while not p.__isEmpty__():
            temp.__push__(p.__pop__())
        while not temp.__isEmpty__():
            elemento = temp.__pop__()
            q.__push__(elemento)
            p.__push__(elemento)


                    # FUNÇÃO QUE ESVAZIA A PILHA RECURSIVAMENTE 

                    # def __esvaziar_pilha_recursivamente__(pilha):
                    #     if pilha.__isEmpty__():  
                    #         return
                    #     pilha.pop__() 
                    #     __esvaziar_pilha_recursivamente__(pilha)


    
   