# detector de palíndromo
frase = str(input('Digite uma palavra, frase ou nome qualquer: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('O inverso de {} é {}'.format(junto, inverso))
    print('Temos um PALÍNDROMO!')
else:
    print('O inverso de {} é {}'.format(junto, inverso))
    print('A frase digitada não é um palíndromo.')

# anotaram a data da maratona
# apos a sopa
# a torre da derrota
# o lobo ama o bolo
# a sacada da casa