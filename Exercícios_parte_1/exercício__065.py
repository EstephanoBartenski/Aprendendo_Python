# maior e menor valores
resp = 'S'
maior = menor = soma = 0
num = float(input('Digite um número qualquer: '))
resp = str(input('Quer continuar? [S/N] ')).upper().strip()
cont = 1
maior = menor = soma = num
while resp in 'Ss':
    num = float(input('Digite um número qualquer: '))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / cont
print('Você digitou {} números e a média deles foi {:.2f}.'.format(cont, media))
print('O maior valor foi {:.2f} e o menor foi {:.2f}.'.format(maior, menor))
