# aprovando empréstimos
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
v = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o salário do comprador? R$'))
a = float(input('Quantos anos de financiamento? '))
prestação = v/(a*12)
if prestação <= (30/100)*s:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(v, a, prestação))
    print('Empréstimo {}CONCEDIDO!{}'.format(cores['verde'], cores['limpa']))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(v, a, prestação))
    print('Como o valor da prestação excede 30% de seu salário,')
    print('Empréstimo {}NEGADO!{}'.format(cores['vermelho'], cores['limpa']))
