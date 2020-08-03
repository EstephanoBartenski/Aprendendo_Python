# game: pedra, papel e tesoura
from time import sleep
from random import choice
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
pl = int(input('Qual é a sua jogada?'))
if pl == 0:
    pl = 'PEDRA'
    print('JO')
    sleep(1)
    print('KEN')
    sleep(2)
    print('PO!!!')
elif pl == 1:
    pl = 'PAPEL'
    print('JO')
    sleep(1)
    print('KEN')
    sleep(2)
    print('PO!!!')
elif pl == 2:
    pl = 'TESOURA'
    print('JO')
    sleep(1)
    print('KEN')
    sleep(2)
    print('PO!!!')
else:
    print('Você precisa escolher uma das opções acima!!!')

pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])

if pl == pc:
    print('{}\n'
          'Computador jogou {}\n'
          'Jogador jogou {}\n'
          '{}\n'
          'EMPATE!'.format(12*'-=', pc, pl, 12*'-='))
elif pc == 'PEDRA' and pl == 'PAPEL':
    print('{}\n'
          'Computador jogou {}\n'
          'Jogador jogou {}\n'
          '{}\n'
          'JOGADOR VENCE!'.format(12*'-=', pc, pl, 12*'-='))
elif pc == 'PEDRA' and pl == 'TESOURA':
    print('{}\n'
          'Computador jogou {}\n'
          'Jogador jogou {}\n'
          '{}\n'
          'COMPUTADOR VENCE!'.format(12*'-=', pc, pl, 12*'-='))
elif pc == 'PAPEL' and pl == 'PEDRA':
    print('{}\n'
          'Computador jogou {}\n'
          'Jogador jogou {}\n'
          '{}\n'
          'COMPUTADOR VENCE!'.format(12*'-=', pc, pl, 12*'-='))
elif pc == 'PAPEL' and pl == 'TESOURA':
    print('{}\n'
          'Computador jogou {}\n'
          'Jogador jogou {}\n'
          '{}\n'
          'JOGADOR VENCE!'.format(12*'-=', pc, pl, 12*'-='))
elif pc == 'TESOURA' and pl == 'PEDRA':
    print('{}\n'
          'Computador jogou {}\n'
          'Jogador jogou {}\n'
          '{}\n'
          'JOGADOR VENCE!'.format(12*'-=', pc, pl, 12*'-='))
elif pc == 'TESOURA' and pl == 'PAPEL':
    print('{}\n'
          'Computador jogou {}\n'
          'Jogador jogou {}\n'
          '{}\n'
          'JOGADOR VENCE!'.format(12*'-=', pc, pl, 12*'-='))


