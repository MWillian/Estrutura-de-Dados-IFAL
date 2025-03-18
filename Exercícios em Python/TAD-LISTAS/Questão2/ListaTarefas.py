
class ListaTarefas:
    def __init__(self):
        self.capacidade = 3
        self.tarefas = [None] * self.capacidade
        self.tamanho = 0

    def TesteEspacoAlocado(self):
        if self.capacidade != len(self.tarefas):
            return "Tamanhos diferentes"
        else:
            return "Tudo ok"
        
    def VerificarTamanhoInicial(self):
        if self.tamanho != 0:
            return "Tamanho Inicial Incorreto!"
        else:
            return "Tamanho Inicial Correto!"
        
    def VerificaTarefasVazias(self):
        for tarefa in self.tarefas:
            if tarefa is not None:
                return "A lista de tarefas não está corretamente vazia!"
            return "Lista de tarefas está totalmente vazia!"
        
    def AdicionaNoFim(self,tarefa):
        if self.capacidade == self.tamanho:
            return "A lista está cheia"
        self.tarefas[self.tamanho] = tarefa
        self.tamanho += 1
        return "Tarefa adicionada!"
    
    def AdicionarNaPosicao(self, tarefa, posicao):
        if posicao < 0 or posicao >= self.capacidade:
            return "Posicão inválida!"
        if self.capacidade == self.tamanho:
            return "A lista está cheia"
        if self.tarefas[posicao] is None:
            self.tarefas[posicao] = tarefa
            self.tamanho += 1  
            return "Tarefa adicionada"
        atual = tarefa  
        for i in range(posicao, self.tamanho + 1):
            temporario = self.tarefas[i]  
            self.tarefas[i] = atual       
            atual = temporario
            print("Tarefa Adicionada")
        self.tamanho += 1  

    def ObterTarefa(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            return "Posição inválida"
        if self.tarefas[posicao] is None:
            return "Não existem tarefas nesta posição"
        return self.tarefas[posicao]
    
    def RemoverTarefa(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            raise ValueError("Posição inválida!")
        for i in range(posicao, self.tamanho - 1):
            self.tarefas[i] = self.tarefas[i + 1]
        self.tarefas[self.tamanho - 1] = None
        self.tamanho -= 1
        return "Tarefa removida com sucesso!"

    def ContemTarefa(self,tarefa):
        for i in self.tarefas:
            if i == tarefa:
                return "A tarefa digitada está na lista!"
        return "A tarefa não está na lista!"

    def TamanhoLista(self):
        return self.tamanho