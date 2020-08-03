# jogo da adivinhação 2.0
from random import randint
num = randint(0, 5)
cont = 0
print('Olá, sou seu computador...\n'
      'Acabei de pensar em um número inteiro entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')
tent = int(input('Qual é seu palpite? '))
while num > tent:
    print('Mais... Tente mais uma vez!')
    tent = int(input('Qual é seu palpite? '))
    cont += 1
while num < tent:
    print('Menos... Tente mais uma vez!')
    tent = int(input('Qual é seu palpite? '))
    cont += 1
if num == tent:
    cont += 1
    if cont == 1:
        print('Acertou de primeira!! Parabéns!')
    else:
        print('Acertou com {} tentativas. Parabéns!'.format(cont))
