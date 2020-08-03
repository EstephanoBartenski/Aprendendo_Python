# números primos
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}
num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num+1):
    div = num / c
    if (num % c) == 0:
        cont = cont + 1
        print(('{}{}{}'.format(cores['verde'], c, cores['limpa'])), end=' ')
    if (num % c) != 0:
        print(('{}{}{}'.format(cores['vermelho'], c, cores['limpa'])), end=' ')
print('\n'
      'O número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('E isso significa que ele é um número PRIMO!')
else:
    print('E isso significa que ele NÃO É um número primo!')