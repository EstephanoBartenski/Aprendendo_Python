# sequência de Fibonacci
print('{}\n'
      'SEQUÊNCIA DE FIBONACCI\n'
      '{}'.format('-'*22, '-'*22))
termos = int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print('{} → {} → '.format(t1, t2), end='')
cont = 3
while cont <= termos:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    print('{} → '.format(t3), end='')
    cont += 1
print('FIM')

