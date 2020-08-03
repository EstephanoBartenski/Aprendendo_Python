# atributos


class Pessoa:
    num_de_pessoas = 0

    @classmethod
    def num_de_pessoas_(cls):
        return cls.num_de_pessoas

    @classmethod
    def add_pessoa(cls):
        cls.num_de_pessoas += 1

    def __init__(self, nome):
        self.nome = nome
        Pessoa.add_pessoa()


p1 = Pessoa('João')
p2 = Pessoa('Zuleide')
p3 = Pessoa('Orimberto')
# print(Pessoa.num_de_pessoas)
print(Pessoa.num_de_pessoas_())

# Pessoa.num_de_pessoas = 55
# print(Pessoa.num_de_pessoas)
# print(p1.num_de_pessoas)
# print(p1.num_de_pessoas)



# aquele num de pessoas que eu deixei lá em cima, fora/antes no init
# vale pra galera toda!! não vai mudar de pessoa pra pessoa
# então posso chamar aquilo pra qualquer pessoa
# e mudar a qualquer tempo, fazendo a classe+aquilo recebe tal
# aí posso fazer contagem hehe
# mas a ideia de constante é a mais útil mesmo, tipo gravidade sl
# algo que é sempre -9.8 m/s²

# class methods
# a ideia é que fazem referência à classe inteira (método da classe),
# e não algum outor método dessa classe