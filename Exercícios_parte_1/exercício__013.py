# reajuste salarial
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario*1.15
print('Um funcionário que ganhava R${:.2f}, com o novo reajuste de 15%, receberá R${:.2f}'.format(salario, novo))
