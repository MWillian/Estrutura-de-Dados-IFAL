# novoInicio: Ini = (Ini + 1) % N
# fimFIla: ((Ini + Tam ) % N) - 1
# próxima posição disponível: # fimFIla: ((Ini + Tam ) % N)


class FilaArray:

    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.tamanho = 0
        self.inicio = 0
    
    def filaCheia(self):
        pass
    
    def __len__(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0

    def dequeue(self):
        if self.is_empty():
            raise ValueError('A Fila está vazia')
        result = self.dados[self.inicio]
        self.dados[self.inicio] = None
        self.inicio = (self.inicio + 1)%len(self.dados)
        self.tamanho -= 1
        return result

    def altera_tamanho (self,novo_tamanho):
        dados_antigos = self.dados
        self.dados = [None]*novo_tamanho
        posicao = self.inicio
        for k in range(self.tamanho):
            self.dados[k] = dados_antigos[posicao]
            posicao = (posicao+1)%len(dados_antigos)
        self.inicio = 0

    def diminui_tamanho (self):
        if 0 < self.tamanho < len(self.dados)//4:
            self.altera_tamanho(len(self.dados)//2)

    def is_full(self):
        return self.tamanho == self.capacidade

    def enqueue(self,e):
        if self.tamanho == len(self.dados):
            self.altera_tamanho(2*len(self.dados))
        disponivel = (self.inicio + self.tamanho) % len(self.dados)
        self.dados[disponivel] = e
        self.tamanho += 1

    def first(self):
        if self.is_empty():
            raise ValueError("A fila está vazia")
        return self.dados[self.inicio]

    def rodar(self):
        if self.is_full():
            raise ValueError('A fila está cheia')
        self.enqueue(self.dequeue())

        
    def __str__(self):
        result = "["
        posicao = self.inicio
        for k in range(self.tamanho):
            result += str(self.dados[posicao]) + ", "
            posicao = (posicao + 1) % len(self.dados)  
        if result.endswith(", "): 
            result = result[:-2]
        result += "]"
        return result


