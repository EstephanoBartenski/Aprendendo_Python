# análise de dados em uma tupla
lista = (int(input('Digite um número inteiro: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {lista}.')
if lista.count(9) == 1:
    print(f'O valor 9 apareceu {lista.count(9)} vez.')
else:
    print(f'O valor 9 apareceu {lista.count(9)} vezes.')
print(f'O valor {lista[2]} apareceu na 3ª posição.')
par = 0
for cont in range(0, len(lista)):
    if lista[cont] % 2 == 0:
        par += 1
print(f'Foram digitados {par} valores pares.')

# outra forma de fazer as primeiras 5 linhas
'''n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
lista = (n1, n2, n3, n4)'''