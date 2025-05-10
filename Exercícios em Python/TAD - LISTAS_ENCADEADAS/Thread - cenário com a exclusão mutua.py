import threading
from Lista_Encadeada import *
from Noh import *
import time


# Instância do bloqueio de acesso (Lock)
lock = threading.Lock()

# Variáveis simbólicas para exibir a ordem dos Nós adicionados e removidos
contador_insercao = 1
contador_remocao = 1

# Função para inserir Nós no fim na lista. A quantidade de Nós é recebida como parâmetro na função. 
# Para visualizar o estado da lista, os valores de cada Nó são retornados a cada inserção ou remoção.
def inserirXVezes(lista:ListaNaoOrdenada,quant):
    global contador_insercao

    # o lock aqui protege toda a área região crítica de ser acessadas por outras Threads.
    with lock: 
        for i in range(0,quant):
            time.sleep(5)
            print(f"Adicionando o {contador_insercao}º nó.")
            lista.add_fim(i)
            lista.print_lista()
            print()
            contador_insercao +=1
        print("Inserção Finalizada")


# Função para remover o Nó da lista. A remoção ocorre no começo da lista.
def removerXVezes(lista:ListaNaoOrdenada,quant):
    global contador_remocao

    # o lock aqui protege toda a área região crítica de ser acessadas por outras Threads.
    with lock:
        for i in range(0,quant):
            time.sleep(5)
            print(f"Realizando a {contador_remocao}ª remoção.")
            lista.remove_first()
            lista.print_lista()
            print()
            contador_remocao +=1
        print("Remoção Finalizada")


# Instância da lista encadeada
ListaExemplo = ListaNaoOrdenada()


# Criação das Threads. Cada Thread recebe como parãmetro a função que deve ser executada, e seus argumentos.
Thread1 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 50))
Thread2 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 50))
Thread3 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 60))
Thread4 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 60))


# Inicializando as threads e finalizando as threads
# O método .join impede que a mesma Thread instânciada seja chamada sem que esta mesma Thread seja finalizada.
Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()

Thread1.join()
Thread2.join()
Thread3.join()
Thread4.join()