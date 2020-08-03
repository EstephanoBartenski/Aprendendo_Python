try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário não informou dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'O resultado da divisão foi {r}.')
finally:
    print('Volte sempre, gafanhoto!')