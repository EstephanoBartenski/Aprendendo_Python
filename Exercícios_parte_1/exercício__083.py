# validando expressões matemáticas
expressão = str(input('Digite uma expressão matemática qualquer: '))
if expressão.count('(') == expressão.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')

# nessa solução acima, ))) 3 + 1 ((( seria aceito como válido
# uma forma correta seria:

expressão = str(input('Digite a expressão: '))
pilha = list()
for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
