i = int(input('Digite um número para o início: '))
f = int(input('Digite um número para o final: '))
p = int(input('Digite um número para o passo: '))
for c in range(i, f+1, p):
    print(c)
print('{}FIM{}'.format('='*5, '='*5))

s = 0
for c in range(0,4):
    n = int(input('Digite um númeoro inteiro: '))
    s += n #isso é a mesma coisa que s = s+n
print('O somatório de todos os valores foi {}.'.format(s))