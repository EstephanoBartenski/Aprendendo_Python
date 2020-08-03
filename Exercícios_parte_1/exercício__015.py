# aluguel de carros
d = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
v = float(d*60.00+km*0.15)
print('O total a pagar é de R${:.2f}'.format(v))
