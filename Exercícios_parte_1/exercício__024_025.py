# verificando as primeiras letras de um texto
# basicamente queremos verificar se você nasceu em alguma cidade que tem 'Santo' no nome
city = str(input('Em que cidade você nasceu?'))
cityx = city.strip()
cityxx = cityx.lower()
print('santo' in cityxx)

# outra forma de resolver, principalmente se for pra ver se tem santo no início
# santo tem 5 letras, lembre-se disso
# também se lembre de que nossa contagem começa em 0, santo seria 01234
# e se lembre que o último nunca é pego (no caso o 4)
city = str(input('Em que cidade você nasceu?')).strip()
print(city[:5].lower() == 'santo')

# procurando uma string dentro de outra
# seu nome tem Silva nele, em qualquer parte?
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva?')
print('silva' in nome.lower())