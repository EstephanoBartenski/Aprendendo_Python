# funções para sortear e somar
def sorteia(lista): # por algum motivo, se definir essa lista aqui como lista = list() vai dar m*
    print('Sorteando 5 valores:', end=' ')
    for c in range(0, 5):
        lista.append(randint(1, 10))
    for c in range(0, 5):
        print(lista[c], end=' ')
        sleep(0.25)
    print('PRONTO!')


def somapar(lista): # mesma coisa aqui
    pares = list()
    for c in range(0, 5):
        if lista[c] % 2 == 0:
            pares.append(lista[c])
    print(f'A soma dos pares da lista {lista} resulta em {sum(pares)}.')


# programa principal
from random import randint
from time import sleep
numeros = list()
sorteia(numeros)
somapar(numeros)
