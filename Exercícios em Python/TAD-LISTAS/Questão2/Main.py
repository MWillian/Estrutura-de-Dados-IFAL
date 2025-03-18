from ListaTarefas import ListaTarefas

class Tarefa:
    def __init__(self,descricao,prioridade):
        self.descricao = descricao
        self.prioridade = self.ValidarPrioridade(prioridade)
    def ValidarPrioridade(self,prioridade):
        if prioridade != "Alta" and prioridade != "Média" and prioridade != "Baixa":
            raise ValueError("Prioridade Inválida! Use Alta, Média ou Baixa.")
        return prioridade
    def __str__(self):
        saida = "Tarefa: " + self.descricao + " (Prioridade: "+self.prioridade+")"
        return saida

t1 = Tarefa("lavar","Baixa")
t2 = Tarefa("passar","Alta")

