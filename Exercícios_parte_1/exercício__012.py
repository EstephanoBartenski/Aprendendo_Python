# calculando descontos
p = float(input('Qual é o preço do produto? R$'))
d = p-(p*(5/100))
print('O produto que custava R${:.2f}, na promoção com desconto de 5% irá custar R${:.2f}'.format(p, d))


