# maior e menor da sequência
maior = 0
menor = 0
for pessoa in range(1, 11):
    peso = float(input('Qual o peso da {}ª pessoa (em kg)? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.2f} Kg'.format(maior))
print('O menor peso lido foi de {:.2f} Kg'.format(menor))

