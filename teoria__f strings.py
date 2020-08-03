# foi introduzido com o python 3.6
# essa técnica chama-se interpolação dentro de strings

a = b = c = 2.50

# ao invés de:
print('A soma de {} com {} vale {}'.format(a, b, c))

# posso fazer
print(f'A soma de {a:.2f} com {b:.2f} vale {c:.2f}.')

nome = 'José'
salario = 9878.78

print(f'O {nome:-^20} ganha {salario:.2f} por mês.')

# SACA SÓ ISSO!! Dá pra fazer fstring só em um elemento ali!!!
print('--' * 3, f'SORTEANDO {} BAGULHOS', '--' * 3)