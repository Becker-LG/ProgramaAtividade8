while True:
    try:
        alunosX = int(input('Quantidade de Alunos:'))
        for i in range(alunosX):
            print('teste')
        break
    except:
        print('Não foi inserido um número, tente novamente!')
        continue