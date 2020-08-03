# custo da viagem
d = float(input('Qual é a distância da sua viagem em km? '))
p1 = d*0.5
p2 = d*0.45
if d<= 200:
    print('O preço da sua passagem será de R${:.2f}'. format(p1))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(p2))

