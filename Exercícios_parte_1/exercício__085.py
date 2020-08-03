lista = list()
pares = list()
impares = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    lista.append(n)
print('--' * 50)
print(f'Você digitou os valores: {lista}')
for v in range(0, len(lista)):
    if lista[v] % 2 == 0:
        pares.append(lista[v])
    else:
        impares.append(lista[v])
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores ímpares digitados foram: {sorted(impares)}')
print('--' * 50)

