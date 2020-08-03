# fatorial usando o for agora
n = int(input('Digite um número inteiro para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c  #f *= n
    c = c - 1   #c -= 1
print(f)

