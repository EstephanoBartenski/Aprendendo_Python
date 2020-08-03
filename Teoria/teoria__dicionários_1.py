filme1 = {'título':'BladeRunner 2049',
         'ano':2017,
         'diretor':'VillaNova'
         }
filme2 = {'título':'No Country for Old Men',
         'ano':2007,
         'diretor':'Coen Brothers'
         }
filme3 = {'título':'Captain Fantastic',
         'ano':2016,
         'diretor':'Matt Ross'
         }
print(filme1.values())
print(filme1.keys())
print(filme1.items())

print()

for k, v in filme1.items():
    print(f'O {k} é {v}.')

print()

# juntando lista e dicionários
locadora = [filme1, filme2, filme3]
print(locadora[0]['ano'])
print(locadora[2]['título'])

print()

# cuidado na hora de refenciar (uso de aspas duplas dentro das simples)
pessoas = {'nome':'Estephano', 'idade':25, 'sexo':'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print()

for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo'] #tirou
pessoas['nome'] = 'Josnei' #trocou
pessoas['peso']: 76.8 #adicionou

pessoas.clear() # FUNCIONA com dicionários também