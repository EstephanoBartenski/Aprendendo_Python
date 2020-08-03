# jogo de dados em python
from random import randint
from time import sleep
from operator import itemgetter
sorteios = {'Jogador [1]':randint(1, 6),
            'Jogador [2]':randint(1, 6),
            'Jogador [3]':randint(1, 6),
            'Jogador [4]':randint(1, 6)}
ranking = list()
print('        VALORES SORTEADOS:')
for k, v in sorteios.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(0.5)
print('--' * 18)
sleep(0.5)
print('        < RANKING >')
ranking = sorted(sorteios.items(), key=itemgetter(1), reverse=True) # 0 aqui seria chave, 1 seria valor
for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar: {v[0]} com {v[1]}')
    sleep(0.5)

