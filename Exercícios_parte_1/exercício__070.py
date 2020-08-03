# estatísticas em produtos
produto = ' '
somapreço = produtosmil = barato = cont = 0
continua = 'S'
print('{}\n'
      '    PYTHON STORE\n'
      '{}'.format('-' * 20, '-' * 20))
while continua == 'S':
      produto = str(input('Digite o nome do produto adquirido: ')).strip().capitalize()
      preço = float(input('Preço: R$'))
      somapreço += preço
      cont += 1
      if cont == 1 or preço < barato:
            barato = preço
            nomebarato = produto
      if preço > 1000.00:
            produtosmil += 1
      continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
      while continua not in 'SN':
            continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print(f'\n'
      f'O total da compra foi {somapreço:.2f}.')
print(f'Você comprou {produtosmil} produtos que custaram mais que R$1000.00.')
print(f'O produto mais barato foi {nomebarato} que custou R${barato:.2f}.')
print('\n'
      '{:-^40}'.format('FIM DO PROGRAMA'))
