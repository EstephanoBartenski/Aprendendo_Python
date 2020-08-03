# radar eletrônico
v = float(input('Qual é a velocidade atual do seu carro em km/h? '))
multa = ((v-80)*7)
if v<= 80.0:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('VOCÊ FOI MULTADO! Excedeu o limite de velocidade que é de 80 km/h\nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
