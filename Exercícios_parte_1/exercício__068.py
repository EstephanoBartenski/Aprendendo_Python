# jogo PAR ou ÍMPAR
from random import randint
from time import sleep
numcomputador = randint(0, 10)
print('{}\n'
      '  BORA JOGAR PAR OU ÍMPAR\n'
      '{}'.format('-==-' * 7, '-==-' * 7))
sleep(1)
numjogador = int(input('Diga um valor: '))
jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
cont = 0
sleep(1)
while True:
    if jogador in 'Pp':
        jogador = 'PAR'
        computador = 'ÍMPAR'
    else:
        jogador = 'ÍMPAR'
        computador = 'PAR'
    result = numjogador + numcomputador
    if result % 2 == 0 and jogador == 'PAR':
        deu = 'PAR'
        print(f'\n'
              f'Você jogou {numjogador} e o computador jogou {numcomputador}.\n'
          f'Total deu {result} que é {deu}!')
        print('Parabéns, VOCÊ GANHOU!\n'
              'Vamos jogar novamente...\n')
        cont += 1
        sleep(1)
        numjogador = int(input('Diga um valor: '))
        jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    elif result % 2 != 0 and jogador == 'ÍMPAR':
        deu = 'ÍMPAR'
        print(f'\n'
              f'Você jogou {numjogador} e o computador jogou {numcomputador}.\n'
              f'Total deu {result} que é {deu}!')
        print('Parabéns, VOCÊ GANHOU!\n'
              'Vamos jogar novamente...\n')
        cont += 1
        sleep(1)
        numjogador = int(input('Diga um valor: '))
        jogador = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    elif result % 2 == 0 and jogador == 'ÍMPAR':
        deu = 'PAR'
        print(f'\n'
              f'Você jogou {numjogador} e o computador jogou {numcomputador}.\n'
              f'Total deu {result} que é {deu}!')
        sleep(1)
        print('\n'
              'Você PERDEU!')
        break
    elif result % 2 != 0 and jogador == 'PAR':
        deu = 'ÍMPAR'
        print(f'\n'
              f'Você jogou {numjogador} e o computador jogou {numcomputador}.\n'
              f'Total deu {result} que é {deu}!')
        sleep(1)
        print(f'\n'
              'Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {cont} vezes')

# mais uma forma de fazer isso e em menos linhas...
'''from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P /I] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')'''
