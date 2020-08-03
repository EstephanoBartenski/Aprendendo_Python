from datetime import date
hoje = date.today().year
totmenor = 0
totmaior = 0
for pessoa in range(1, 5):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = hoje - nasc
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade!'.format(totmaior, totmenor))