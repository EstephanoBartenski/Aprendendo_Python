print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('-' * 39)

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor',
            4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)

for c in range(0, len(produtos), 2):                # aqui tem um segredinho, o ,2 garante que vamos pegando de 2 em 2
    print(f'{produtos[c]:.<30}R${produtos[c + 1]:7.2f}')
print('-' * 39)
