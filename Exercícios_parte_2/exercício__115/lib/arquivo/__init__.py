from ex115.lib.interface import cabeçalho


def testfile(nome):
    try:
        a = open(nome, 'rt')  # rt significa 'read text'
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createfile(nome):
    try:
        a = open(nome, 'wt+')  # write texte e se não existir, crie
        a.close()
    except:
        print('\033[1;31mHouve um erro na criação do arquivo.\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def readfile(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[1;31mErro ao ler o arquivo.\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')  # separo e dado será uma lista
            dado[1] = dado[1].replace('\n', '')  # lá no cadastrar eu coloquei \n pra ficar ok, agr tiro
            print(f'{dado[0]:<34}{dado[1]:>3} anos')  # dado 0 nome e dado 1 idade


def cadastrar(arquivo, nome='<desconhecido>', idade=0):
    try:
        a = open(arquivo, 'at')  # a é de append, ficando append text
    except:
        print('\033[1;31mErro ao ler o arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[1;31mErro ao escrever os dados.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


def excluir(arquivo, nome):
    try:
        with open(arquivo, 'r+') as a:
            b = a.readlines()
            a.seek(0)
            for line in b:
                if nome not in line:
                    a.write(line)
            a.truncate()
    except:
        print('\033[1;31mERRO! Digite o nome de quem deseja remover\033[m')
    else:
        print(f'{nome} removido com sucesso.')


def alterar(arquivo, quem, nome):
    try:
        a = open(arquivo, 'rt')
        data = a.read()
        data = data.replace(quem, nome)
        a.close()
        a = open(arquivo, 'wt')
        a.write(data)
        a.close()
    except:
        print('\033[1;31mERRO! Tente novamente.\033[m')
    else:
        print(f'Dados alterados com sucesso.')

# readlines() pega cada linha e põe dentro de uma lista
# read() lê como está lá
