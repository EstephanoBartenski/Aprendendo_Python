# soma dos pares
soma = 0
cont = 0
contpares = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    cont = cont + 1
    if (n % 2) == 0:
        soma = soma + n
        contpares = contpares + 1
if n != 1:
    print('Você informou {} números. Deles, {} são pares.\n'
          'A soma desses pares apenas resulta em: {}'.format(cont, contpares, soma))
else:
    print('Você informou {} números. Deles, {} é par.\n'
          'A soma só dele resulta em: {}'.format(cont, contpares, soma))
