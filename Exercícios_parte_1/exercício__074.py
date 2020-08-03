# maior e menor valores em tupla
from random import randint
sorteio = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),
           randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram: {}.'.format(sorteio))
print('O maior valor sorteado foi {}.'.format(max(sorteio)))
print('O menor valor sorteado foi {}.'.format(min(sorteio)))