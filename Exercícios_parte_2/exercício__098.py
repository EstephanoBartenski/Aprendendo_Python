# função de contador
def contador(inicio, fim, passo):
    if inicio < fim:
        print('--' * 19)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' ')
            sleep(0.25)
        print('FIM!')
        print('--' * 19)
    else:
        print('--' * 19)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for c in range(inicio, fim - 1, -passo):
            print(f'{c}', end=' ')
            sleep(0.25)
        print('FIM!')
        print('--' * 19)


def contadorinterativo():
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('De quanto em quanto: '))
    if passo < 0:
        passo = passo * (-1)
    if passo == 0:
        passo = 1
    contador(inicio, fim, passo)


# programa principal
from time import sleep
contador(1, 10, 1)
contador(10, 0, 2)
contadorinterativo()