# static classes


class Math:

    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def dobro(x):
        return x * 2


print(Math.soma(5, 5))
print(Math.dobro(10))


# a ideia aqui é agrupar diversas funções (def) dentro de uma classe
# a ideia é que fazem algo, mas não mudam nada no resto
# não preciso passar parâmetro self para funções dentro disso,
# porque não vão pegar nada, são só elas sozinhas ali
# a ideia é organização mesmo, porque bastaria fazer globalmente (fora de tudo)