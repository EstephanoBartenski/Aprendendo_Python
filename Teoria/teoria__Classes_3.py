# inheritance
class Pet:
    def __init__(self, nome, idade):
        self.nome = nome
        self. idade = idade

    def mostre(self):
        print(f'Eu sou {self.nome}, tenho {self.idade} ano(s)!')

    def fale(self):
        print('Não sei o que devo falar!!!')


class Gato(Pet):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def fale(self):
        print('Miau')

    def mostre(self):
        print(f'Eu sou {self.nome}, tenho {self.idade} ano(s) e sou {self.cor}.')


class Cachorro(Pet):
    def fale(self):
        print('Auau')


class Peixe(Pet):
    pass


p = Pet('Bambam', 2)
p.mostre()
p.fale()
# c = Gato('Thor', 3)
# c.mostre()
# c.fale()
d = Cachorro('Belinha', 6)
d.mostre()
d.fale()
e = Peixe('Bolhas', 10)
e.mostre()
e.fale()

c = Gato('Thorzito', 3, 'cinza c/ branco')
c.mostre()
c.fale()


# note que gato() e cachorro() tem uma parte repetida, a única diferença é o fale
# posso criar uma calsse que contenha o que for repetido
# e deixar essas duas pertencendo à ela
# se tenho algo repetido na classe mãe e nas classes filhas,
# o que tiver nas classes filhas vão sobrepor a da classe mãe
# por ser mais específica

# é importante criar o fale na classe mãe mesmo que seja substituído depois,
# porque posso criar algo diferente depois, como um peixe, nesse exemplo

# super() é uma forma de pedir atributos num classe filha,
# puxando o que pedir lá da classe mãe
# mas sem atrapalhar a classe mãe (pode ser perigoso mudar algo lá sl)
# basicamente o super() manda lá pra cima no init da mãe pra pedir o que eu preciso
# e o que eu não tiver lá em cima eu defino na classe filha mesmo

# um exemplo para inheritance:
# em uma escola temos professores, alunos, servidores
# alguns atributos são diferentes pra cada coisa
# materias p/ prof, notas/turma p/ alunos, área/função p/servidores
# então cada um deles tem algo específico, mas têm algo em comum também
# são pessoas
# posso ter uma classe mãe de pessoas de uma instituição
# e conforme o que for essa pessoa eu pego específico o que precisar
# mas todos os dados simples que todos têm eu pego na função mãe
# nome CPF RG idade sexo filiação etc
