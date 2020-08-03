# dividindo valores em várias listas
lista = list()
pares = list()
impares = list()
resp = 'S'
while resp in 'Ss':
    lista.append(int(input('Digite um número inteiro: ')))
    if lista[-1] % 2 == 0:
        pares.append(lista[-1])
    elif lista[-1] % 2 == 1:
        impares.append(lista[-1])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while True:
        if resp not in 'SNsn':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        else:
            break
print('--' * 15)
print(f'Lista completa: {lista}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos ímpares: {impares}')

# outra forma de fazer o par e impar
'''pares = list()
impares = list()
for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)'''