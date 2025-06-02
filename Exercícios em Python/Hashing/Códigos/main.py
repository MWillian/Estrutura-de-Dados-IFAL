# Folding method:
# divida o item em pedaços de tamanhos iguais e some os pedaços

# Exemplo:
# Telefone: (82)7989.1507
# dividindo em grupos de 2: (82,79,89,15,07)
# some-os: 82 + 79 + 89 + 15 + 07 = 272
# Se a tabela tem 11 slots, então 272 % 11 = 8
# O telefone (82)9988.1507 deve ser armazenado na posição 8

# Alguns ‘folding methods’ têm um passo extra: inverter pedaços de maneira alternada
# (82)7989.1507 = (82,79,89,15,07) = (82,97,89,51,07) = 326 % 11 = 7


# Mid-square method: 
# Eleve o item ao quadrado e extraia algumas porções dos dígitos resultantes
# Exemplo:
# Item: 44
# 44^2 = 1936
# extrair os dois dígitos do meio: 93
# 93 % 11 = 5


# Funções hashing para string: 

# Some os códigos ASCII de cada caracter da string, e passe o resultado pelo módulo de 11
# Exemplo: "cat"
# c > 99 / a > 97 / t > 116  = 99 + 97 + 116 = 312 % 11 = 4

def HashParaString(uma_string, tamanho_tabela):
    sum = 0
    for pos in range(len(uma_string)):
        sum = sum + ord(uma_string[pos])
    return sum %tamanho_tabela


# Quando surgirem anagramas de strings, estes terão o mesmo hash.
# Como sulução, multiplica-se o código ASCII do caracter pertencente a string pela sua posição
# Exemplo: 99 * 1 + 97 * 2 + 116 * 3 = 641 % 11 = 3

# Colisões irão acontecer quanddo dois itens são associados ao mesmo slot
# O primeiro método de resolução seria utilizar o open adress e linear probing: se procura sequencialmente o próximo slot disponível

# newhashvalue=rehash(oldhashvalue)
# rehash(pos)=(pos+1)%sizeoftable.

# quadratic probing:
# new_position=(original_position+i2)%table_size


# chaining:
# usa uma estrutura de dados dentro de cada célula da tabela para armazenar múltiplos valores que compartilham o mesmo índice.


