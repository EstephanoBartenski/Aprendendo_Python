# lista de preços com tupla única
print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('-' * 39)

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)

for c in range(0, len(produtos)):
    if c % 2 == 0:                                       # se for par, será nome do produto né
        print(f'{produtos[c]:.<30}', end='')
    if c % 2 == 1:                                      # se for posição impar será o preço né
        print(f'R$ {produtos[c]:6.2f}')
print('-' * 39)
