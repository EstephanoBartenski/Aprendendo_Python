# sorteando um item na lista
import random
a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno')
a4 = input('Quarto aluno')
print('O aluno escolhido aleatoriamente foi: {}'.format(random.choice([a1, a2, a3, a4])))

# alternativamente
lista = [a1, a2, a3, a4]
print('O aluno escolhido aleatoriamente foi: {}'.format(random.choice(lista)))

# escolhendo uma ordem aleatória de alunos
print('A ordem de apresentação será: {}'.format(random.sample([a1, a2, a3, a4], k=4)))

# alternativamente 2.0
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))









