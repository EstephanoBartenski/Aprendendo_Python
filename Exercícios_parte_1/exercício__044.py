# gerenciador de pagamentos
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
print('='*10, 'LOJAS BARTENSKI', '='*10)
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro/cheque (com 10% de DESCONTO)\n'
      '[ 2 ] à vista cartão (com 5% de DESCONTO)\n'
      '[ 3 ] à 2x no cartão (preço NORMAL)\n'
      '[ 4 ] 3x ou mais no cartão (com 20% de JUROS)')
opção = int(input('Qual é a sua opção?'))
if opção == 1:
    vf = 0.9*preço
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, vf))
elif opção == 2:
    vf = 0.95*preço
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, vf))
elif opção == 3:
    vf = preço
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, vf))
elif opção == 4:
    parcelas = int(input('Quantas parcelas você deseja? '))
    vf = 1.2*preço
    juros = vf/parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS\n'
          'Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
        parcelas, juros, preço, vf))
else:
    print('Opção INVÁLIDA de pagamento.\n'
          'Tente novamente!')
