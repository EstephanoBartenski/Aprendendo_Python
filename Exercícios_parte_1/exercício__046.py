# contagem regressiva
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
from time import sleep
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(0.5)
print('{}BUM! BUM! POOOW!{}'.format(cores['vermelho'],cores['limpa']))
