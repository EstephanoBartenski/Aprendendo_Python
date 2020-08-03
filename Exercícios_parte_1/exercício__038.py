# comparando números
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1>n2:
    print('O primeiro valor é maior! ({:.2f} > {:.2f})'.format(n1, n2))
elif n1<n2:
    print('O segundo valor é maior! ({:.2f} > {:.2f})'.format(n2, n1))
elif n1==n2:
    print('Não há valor maior aqui, os dois são iguais! ({:.2f} = {:.2f})'.format(n1, n2))
