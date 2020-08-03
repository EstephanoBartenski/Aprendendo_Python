# função que descobre o maior
def maiormenor(* lista):
    while True:
        resp = int(input('Digite 1 p/ maior ou 2 p/ menor '))
        if resp != 1 and resp != 2:
            print('Ops, digite 1 ou 2!')
        elif resp == 1:
            lista = list()
            qts = int(input('Quantos valores você quer analisar? '))
            if qts <= 0:
                print('Nenhum valor informado!')
            else:
                for c in range(0, qts):
                    lista.append(float(input('Digite um valor: ')))
                print('Analisando os valores...')
                sleep(0.5)
                print(f'Foram informados {len(lista)} valores ao todo.')
                for c in lista:
                    print(f'{c}', end=' ')
                    sleep(0.50)
                print()
                sleep(0.50)
                print(f'O MAIOR valor foi {max(lista):.2f}!')
                break
        elif resp == 2:
            lista = list()
            qts = int(input('Quantos valores você quer analisar? '))
            if qts <= 0:
                print('Nenhum valor informado!')
            else:
                for c in range(0, qts):
                    lista.append(float(input('Digite um valor: ')))
                print('Analisando os valores...')
                sleep(0.5)
                print(f'Foram informados {len(lista)} valores ao todo.')
                for c in lista:
                    print(f'{c}', end=' ')
                    sleep(0.50)
                print()
                sleep(0.50)
                print(f'O MENOR valor foi {min(lista):.2f}!')
                break


# programa principal
from time import sleep
maiormenor()