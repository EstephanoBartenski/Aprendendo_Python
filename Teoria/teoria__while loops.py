# while é tipo o for, mas se eu não sei o limite de parada, não tenho como usar o for
'''r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim!')'''

# outro exemplo, agora de algo que fizemos com o for já
'''c = 1
while c < 11:
    print(c)
    c += 1
print('Fim!')'''

# outro exemplo: quanto digitar o valor 0, aí tem parar
'''n = 1 # isso aqui é só uma pequena gambiarra pra fazer funcionar
while n != 0:
    n = int(input('Digite um número inteiro qualquer: '))
print('Fim!')'''

# mais um exemplo de coisa que já fizemos (contar par e ímpar)
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero inteiro qualquer: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números PARES e {} números ÍMPARES'.format(par, impar))

