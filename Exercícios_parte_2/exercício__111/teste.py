from ex111.utilidades import moeda, dados
p = dados.leiadinheiro('Digite um preço: R$ ')
moeda.resumo(p, 45, 18)

print()

n1 = dados.leiaintv2('Digite um número inteiro: ')
n2 = dados.leiarealv2('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2:.2f}.')
