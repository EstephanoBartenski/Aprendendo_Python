# arquivo do exercício
from ex107 import moeda
preço = float(input('Digite um preço: R$ '))
print(f'A metade de R${preço:.2f} é R${moeda.metade(preço):.2f}.\n'
      f'O dobro de R${preço:.2f} é R${moeda.dobro(preço):.2f}.\n'
      f'Aumentando 10% em R${preço:.2f}, temos R${moeda.aumentar(preço, 10):.2f}.\n'
      f'Diminuindo 10% em R${preço:.2f}, temos R${moeda.diminuir(preço, 10):.2f}.')


