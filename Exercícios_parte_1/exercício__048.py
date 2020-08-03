# soma ímpares múltiplos de 3
soma = 0 # acumulador
cont = 0 # contador
for c in range(1, 501):
    if (c % 3) == 0 and (c % 2) != 0:
        soma = soma + c # isso é um acumulador!
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

# posso fazer soma += c e cont += 1