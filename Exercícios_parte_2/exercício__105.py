# validando e gerando dicionários
def notas(* n, sit=False):
    """
    → Função para analisar notas e situação de um aluno.
    :param n: (aceita várias) Notas do aluno para análise.
    :param sit: (opcional) Adiciona a situação com base na média das notas.
    :return: (dict) Várias informações sobre a situação do aluno.
    → Criado por Estephano Bartenski (28/01/20).
    """
    ficha = dict()
    ficha['total'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)
    ficha['média'] = sum(n) / len(n)
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'BOA'
        elif 5 <= ficha['média'] < 7:
            ficha['situação'] = 'RAZOÁVEL'
        elif ficha['média'] < 5:
            ficha['situação'] = 'RUIM'
    return ficha


# programa principal
resp = notas(5.5, 9.0, 10, 2.5)
print(resp)