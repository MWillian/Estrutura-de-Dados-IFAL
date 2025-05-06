def BuscaSequencia(lista, item):
    pos = 0
    encontrou = False
    tamanho_lista = len(lista)

    while pos < tamanho_lista and not encontrou:
        if lista[pos] == item:
            encontrou = True
        else:
            pos = pos + 1
    return encontrou

def BuscaSequencial2(lista, item):
    for i in range (len(lista)):
        if lista[i] == item:
            return True
    return False

# em ambos os casos temos O(n)

def BuscaSequencialOrdenada (lista, item):
    pos = 0
    encontrou = False
    parar = False
    tamanhoLista = len(lista)
    cont = 0
    while pos < tamanhoLista and not encontrou and not parar:
        if lista[pos] == item:
            encontrou = True
        else:
            if lista[pos] > item:
                parar = True
            else:
                pos = pos + 1
        cont+=1
        print(cont)

# aqui, temos uma lista ordenada onde caso o numero testado na lista seja maior que o item a ser buscado
# já podemos parar o processamento.
# ainda temos custo de processamento O(n)

def BuscaBinaria(lista, item):
    inicio = 0 
    fim = len(lista)-1
    encontrou = False

    while inicio <= fim and not encontrou:
        meio = (inicio + fim)//2
        if lista[meio] == item:
            encontrou = True
        else:
            if item < lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1 
    return encontrou

def BuscaBinariaRecursiva(lista, item):
    if len(lista) == 0:
        return False
    else:
        meio = len(lista)//2
        if lista[meio] == item:
            return True
        else:
            if item < lista[meio]:
                return BuscaBinariaRecursiva(lista[:meio],item)
            else:
                return BuscaBinariaRecursiva(lista[meio+1:],item)

def BuscaBinaria2(lista, item, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista)-1
    
    if inicio > fim:
        return False
    
    meio = (inicio + fim)//2
    if lista[meio] == item:
        return True
    else:
        if item < lista[meio]:
            fim = meio - 1 
            return BuscaBinaria2(lista,item,inicio,fim)
        else:
            inicio = meio + 1
            return BuscaBinaria2(lista, item,inicio,fim)