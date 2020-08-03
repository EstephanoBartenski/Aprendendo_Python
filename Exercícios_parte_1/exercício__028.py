# JOGO DA ADIVINHAÇÃO 1.0
from time import sleep
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-'*18)
print(' ')
sleep(2)
import random
n = [0, 1, 2, 3, 4, 5]
x = int(random.choice(n))
chute = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if chute == x:
    print('VOCÊ GANHOU! Eu realmente havia pensado no número {}, parabéns!'.format(x))
else:
    print('EU GANHEI! Eu havia pensado no número {} e não no {}!'.format(x, chute))


