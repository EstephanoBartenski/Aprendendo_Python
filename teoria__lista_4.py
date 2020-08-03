teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
# galera.append(teste) ISSO AQUI NÃO PODE
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print()

pessoal = [['Joana', 33], ['Marcelo', 45], ['Otávio', 50], ['Jorge', 12], ['Bárbara', 14]]
for p in pessoal:
    print(f'O(a) {p[0]} tem {p[1]} anos de idade.')

