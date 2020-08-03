# caixa eletrônico
print('{}\n'
      'PYTHON BANK FOR DUMMIES\n'
      '{}'.format('=' * 23, '=' * 23))
'''valor = int(input('Que valor você quer sacar? R$'))
total = valor
totalnotas = 0
cedatual = 100
while True:
    if total >= cedatual:
        total -= cedatual
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Total de {totalnotas} cédulas de R${cedatual}.')
        if cedatual == 100:
            cedatual = 50
        if cedatual == 50:
            cedatual = 20
        if cedatual == 20:
            cedatual = 10
        if cedatual == 10:
            cedatual = 5
        totalnotas = 0
        if total == 0:
            break'''

# outra forma
valor = int(input('Que valor você quer sacar? R$'))
nota100 = valor // 100
valor %= 100
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota5 = valor // 5
valor %= 5
print(f"notas de 100 = {nota100}")
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 5 = {nota5}")

