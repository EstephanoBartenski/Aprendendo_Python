# contando pares
for contagem in range(2,52,2):
    print(contagem, end=' ')

# outra forma de fazer
for contagem in range(1,51):
    if (contagem%2) == 0:
        print(contagem, end=' ')
# neste segundo método, a interação é feita de 1 em 1, mesmo que o resultado não seja mostrado. No primeiro método, só
# foi feito metade do serviço (isso ocupa menos processador)
