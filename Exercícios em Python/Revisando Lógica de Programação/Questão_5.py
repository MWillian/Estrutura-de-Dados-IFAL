# Escreva uma função em que, dada uma variável x com algum valor inteiro, temos um novo x de acordo com a seguinte
# regra:

# Se x é par, x = x / 2;
# Se x é impar, x = 3 * x + 1;
# Imprime x;

def comparacao(x):
    if x % 2 == 0:
        x = x = x / 2
    else:
        x = 3 * x + 1
    print(x)
comparacao(5)