# tratando vários números
'''cont = 1
soma = num = 0
while num != 999:
    num = float(input('Digite um número qualquer [999 p/ parar]: '))
    if num != 999:
        soma = soma + num
        cont += 1
    else:
        cont -= 1
print('Você digitou {:.2f} números e a soma entre eles foi {:.2f}'.format(cont, soma))'''

# outra forma
# basta colocar o print do 999 dentro e fora do while, já que o while tem a condição de não ser
# 999, então quando você digitar 999 ele não roda o loop
# lembre-se de colocar o input do num depois de atribuir algo para soma
cont = soma = num = 0
num = float(input('Digite um número qualquer [999 p/ parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = float(input('Digite um número qualquer [999 p/ parar]: '))
print('Você digitou {:.2f} números e a soma entre eles foi {:.2f}. '.format(cont, soma))