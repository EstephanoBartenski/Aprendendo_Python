# palpites para a mega sena
print('--' * 20)
print('          JOGA NA MEGA SENA')
print('--' * 20)
from time import sleep
from random import randint
jogo = [0, 0, 0, 0, 0, 0]
resp = int(input('Quantos jogos você quer que eu sorteie? '))
if resp == 1:
    print('{} SORTEANDO 1 JOGO {}'.format('==' * 5, '==' * 5))
else:
    print('{} SORTEANDO {} JOGOS {}'.format('==' * 5, resp, '==' * 5))
print()
for v in range(1, resp + 1):
    for c in range(0, 6):
        num = randint(0, 60)
        if num not in jogo:
            jogo[c] = num
    jogo.sort()
    print(f'Jogo {v}: {jogo}')
    sleep(0.5)
print()
print('{} < BOA SORTE > {}'.format('==' * 6, '==' * 6))

