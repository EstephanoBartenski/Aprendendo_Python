# calculando um fatorial
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1 # pra começar uma multiplicação limpa, assim como usamos 0 pra começar uma soma limpa
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

# lembrando que no math tem um factorial

