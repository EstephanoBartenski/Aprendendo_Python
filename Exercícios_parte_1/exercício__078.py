lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um número inteiro para a Posição {c + 1}: ')))
print('--' * 30)
print(f'Você digitou os valores {lista}.')
print(f'O maior valor digitado foi {max(lista)} e ele está na Posição ', end='')
posmaior = list()
for i, v in enumerate(lista):
    if v == max(lista):
        posmaior.append((i + 1))
print(posmaior)
print(f'O menor valor digitado foi {min(lista)} e ele está na Posição ', end='')
posmenor = list()
for i, v in enumerate(lista):
    if v == min(lista):
        posmenor.append(i + 1)
print(posmenor)
print('{}'.format('--' * 30))



