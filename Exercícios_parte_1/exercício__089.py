# boletim com listas compostas
from time import sleep
alunos = list()
indnomemedia = list()
lista1 = list()
lista2 = list()
cont = 0
resp = 'S'
while resp in 'S':
    nome = str(input('Nome: ')).strip().capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista1.append(cont)
    lista1.append(nome)
    lista1.append(media)
    indnomemedia.append(lista1[:])
    lista1.clear()
    lista2.append(nome)
    lista2.append(n1)
    lista2.append(n2)
    alunos.append(lista2[:])
    lista2.clear()
    cont += 1
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print()
print('--' * 26)
print('[i]  NOME                                      MÉDIA')
print('--' * 26)
for c in range(0, cont):
    print(' {}  '.format(indnomemedia[c][0]), end='')
    print(' {:<17}             '.format(indnomemedia[c][1]), end='')
    print('{:>17.2f}'.format(indnomemedia[c][2]))
print('--' * 26)
print()
while True:
    notas = int(input('Mostrar notas de qual aluno?\n'
                      '[escolha pelo índice][digite 999 para interromper] '))
    if notas == 999:
        print()
        print('FINALIZANDO...')
        sleep(0.5)
        print('---- VOLTE SEMPRE! ----')
        break
    else:
        print()
        sleep(0.5)
        print('Notas de {} foram {} e {}.'.format(alunos[notas][0], alunos[notas][1], alunos[notas][2]))
        print()