# a ideia do ex085 era trabalho com somente uma lista!
# segredinho já está na linha 3!
lista = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)                      # dá pra fazer append escolhendo a posição onde entra
    else:
        lista[1].append(n)
print('--' * 50)
print(f'Você digitou os valores: {lista}')
lista[0].sort()                                 # IMPORTANTE!!!
lista[1].sort()                         # TENHO QUE FAZER A ESCOLHA DO PEDAÇO ANTES DA FUNÇÃO, À ESQUERDA
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
print('--' * 50)

