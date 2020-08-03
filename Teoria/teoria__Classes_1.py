# classes sempre capitalized
import turtle


class Poligono:
    def __init__(self, lados, nome, tamanho=100, cor='black', espessura=2):
        self.lados = lados
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.espessura = espessura
        self.angulos_internos = (self.lados - 2) * 180
        self.angulo = self.angulos_internos / self.lados

    def draw(self):
        turtle.color(self.cor)
        turtle.pensize(self.espessura)
        for l in range(self.lados):
            turtle.forward(self.tamanho)
            turtle.right(180 - self.angulo)


class Quadrado(Poligono):
    def __init__(self, tamanho=100, cor='black', espessura=2):
        super().__init__(4, 'Quadrado', tamanho, cor, espessura)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

triangulo = Poligono(3, 'Triângulo')
# quadrado = Poligono(4, 'Quadrado', cor='red', espessura=5)
pentagono = Poligono(5, 'Pentágono')
hexagono = Poligono(6, 'Hexágono')

# print(pentagono.lados, pentagono.nome)
# print(quadrado.angulos_internos)  # 360

quadrado = Quadrado(tamanho=200, cor='black')
print(quadrado.lados)  # 4
print(quadrado.angulo)  # 90
# pentagono.draw()

# a ideia da subclasse é reusar parâmetros com o init super p/ não ficar digitando sempre
# super traz para a subclasse tudo o que for especificado

# turtle.done()  # só pra manter a janela aberta


##


import matplotlib.pyplot as plt


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # basicamente ensinando a somar pontos
        if isinstance(other, Ponto):
            x = self.x + other.x
            y = self.y + other.y
            return Ponto(x, y)
        else:
            x = self.x + other
            y = self.y + other
            return Ponto(x, y)

    def plot(self):
        plt.scatter(self.x, self.y)


a = Ponto(3, 4)
b = Ponto(2, 2)
# a.plot()
# plt.show()

c = a + b  # isso dá erro! Precisamos fazer operator overload (será o add lá em cima)
print(c.x, c.y)

d = a + 5  # também preciso ensinar a somar ponto com número (is instance)
print(d.x, d.y)  # ax é 3 + 5 = 8, ay é 4 + 5 = 9

d = a + Ponto(10, 100)
print(d.x, d.y)

# if isinstance(object, type): verifica se o objeto é um tipo tal