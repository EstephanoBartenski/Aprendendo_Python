# analisador de textos
texto = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas apenas é {}'.format(texto.upper()))
print('Seu nome em minúsculas apenas é {}'.format(texto.lower()))
print('Seu nome tem, ao todo, {} letras'.format(len(texto)-texto.count(' ')))
textoseparado = texto.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(textoseparado[0], len(textoseparado[0])))

