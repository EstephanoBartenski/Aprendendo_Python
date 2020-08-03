lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

print(lanche)
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

# nessa segunda forma com o cont é possível eu mostrar a posição (que será o cont) na frente
# de cada item da tupla, colocando {cont} na linha 13 aqui nesse exemplo
# porque daí mostra a posição de cada termo
# MAS TEMOS mais uma maneira de fazer isso, veja:

for posição, comida in enumerate(lanche):
    print(f'Cada {comida} está em sua {posição}')

# usando sorted eu posso ordenar em ordem alfabética, note que o result do sorted
# estará com [], o que significa que virou uma lista
print(sorted(lanche))
print(lanche)

# somando tuplas (lembrando que a+b != b+a
a = (2, 5, 8, 7, 8, 8, 5)
b = (77, 88, 99, 50)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5)) # quantas vezes aparece o 5?
print(c.index(8)) # em que posição está o 8?
print(c.index(5, 2)) # começo a procurar a posição do 5 começando na posição 2

# tuplas aceitam letras e números na mesma tupla
pessoa = ('Estephano', 25, 'M', 78.5)
print(pessoa)

# tuplas também funcionam com max e min (desde que preenchidas por numeros)