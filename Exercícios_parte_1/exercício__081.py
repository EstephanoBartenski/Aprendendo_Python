# extraindo dados de uma lista
# quero qts elementos, ordem decrescente, e se o 5 está na lista
# pessoa digita até não querer mais
lista = list()
resp = 'S'
while resp in 'S':
    # n = int(input('Digite um valor número inteiro: '))
    lista.append(int(input('Digite um valor número inteiro: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while True:
        if resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        else:
            break
lista.sort(reverse=True)
print('--' * 15)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente foram: {lista}')
if lista.count(5) == 0:
    print(f'O valor 5 não foi encontrado na lista.')
elif lista.count(5) == 1:
    print(f'O valor 5 foi encontrado uma vez na lista!')
else:
    print(f'O valor 5 foi encontrado {lista.count(5)} vezes na lista!')