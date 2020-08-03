# vários números com flag
soma = cont = 0
while True:
    num = float(input('Digite um valor [999 p/ parar] '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma:.2f}!')

# cont e soma precisam ficar DEPOIS DO BREAK