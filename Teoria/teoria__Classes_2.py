

class Cachorro:
    def __init__(self, nome='<sem nome>', idade=0, raça='Caramelinho'):
        self.nome = nome
        self.idade = idade
        self.raça = raça
        print(f'{nome}, {idade} anos, {raça}. !BARK!')

    def definir_nome(self, nome):
        self.nome = nome
        return nome

    def definir_idade(self, idade):
        self.idade = idade

    def definir_raça(self, raça):
        self.raça = raça

    def pegar_nome(self):
        return self.nome

    def pegar_idade(self):
        return self.idade

    def pegar_raça(self):
        return self.raça


a = Cachorro()
print(a.raça)
a.definir_nome('Pedrisco')
print(a.nome)
a.definir_idade(6)
print(a.idade)
print(a.pegar_nome(), a.pegar_idade(), a.pegar_raça())

b = Cachorro('Nescau', 3, 'Mestiço')

print()
print('--' * 50)
print()


class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota  # 0 - 10

    def pegar_nota(self):
        return self.nota


class Turma:
    def __init__(self, nome, max_alunos):
        self.nome = nome
        self.max_alunos = max_alunos
        self.alunos = []

    def add_aluno(self, aluno):
        if len(self.alunos) < self.max_alunos:
            self.alunos.append(aluno)
            return True  # pra me avisar se de certo
        return False

    def pegar_media(self):
        v = 0
        for aluno in self.alunos:
            v += aluno.pegar_nota()
        return v / len(self.alunos)


s1 = Aluno('Tim', 19, 7.5)
s2 = Aluno('Bill', 19, 7.0)
s3 = Aluno('Jill', 18, 9.1)
t = Turma('Ciência', 2)
t.add_aluno(s1)
t.add_aluno(s2)
print(t.add_aluno(s3))  # false
print(t.alunos[0].nome)
print(t.pegar_media())

