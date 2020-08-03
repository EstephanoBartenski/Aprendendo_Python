# analisador de triângulos 1.0
print('-='*20)
print('       ANALISADOR DE TRIÂNGULOS')
print('-='*20)
print(' ')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a+b)>c and (b+c)>a and (b+a)>c:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

