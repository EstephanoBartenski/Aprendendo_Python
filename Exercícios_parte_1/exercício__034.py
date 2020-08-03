# aumentos múltiplos 1250 10%     15%
sal = float(input('Qual é o salário do funcionário? R$'))
sal10 = sal*(1.10)
sal15 = sal*(1.15)
if sal <= 1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, sal15))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, sal10))


