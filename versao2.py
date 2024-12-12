from classes import Aluno
from classes import Professor
from classes import SegmentoEnsino
from classes import Turma
from classes import Disciplinas

#CRIAÇÃO DOS OBJETOS ==================================================================================================================================================================

segmentoEnsino1 = SegmentoEnsino('Ensino Medio', ['Mecatrônica', 'Eletromecânica', 'Informática'], 'Sim')
segmentoEnsino2 = SegmentoEnsino('Ensino Superior', ['Ciências da Computação', 'Pedagogia'], 'Sim')
segmentosEnsino = [segmentoEnsino1, segmentoEnsino2]

turma1 = Turma('turma1', segmentosEnsino[0].segmento, segmentosEnsino[0].cursos[0], '2024', [], [], [], 'Sim')

aluno1 = Aluno('aluno1-1', '1-1', '1-1', '1-1', 'aluno1-1', 'aluno1-1@gmail.com', 'aluno1-1', 'Sim', turma1, '', 'pai1-1@gmail.com', '1-1', segmentosEnsino[0].segmento)
aluno2 = Aluno('aluno1-2', '1-2', '1-2', '1-2', 'aluno1-2', 'aluno1-2@gmail.com', 'aluno1-2', 'Sim', turma1, '', 'pai1-2@gmail.com', '1-2', segmentosEnsino[0].segmento)
aluno3 = Aluno('aluno1-3', '1-3', '1-3', '1-3', 'aluno1-3', 'aluno1-3@gmail.com', 'aluno1-3', 'Sim', turma1, '', 'pai1-3@gmail.com', '1-3', segmentosEnsino[0].segmento)
aluno4 = Aluno('aluno1-4', '1-4', '1-4', '1-4', 'aluno1-4', 'aluno1-4@gmail.com', 'aluno1-4', 'Sim', turma1, '', 'pai1-4@gmail.com', '1-4', segmentosEnsino[0].segmento)
aluno5 = Aluno('aluno1-5', '1-5', '1-5', '1-5', 'aluno1-5', 'aluno1-5@gmail.com', 'aluno1-5', 'Sim', turma1, '', 'pai1-5@gmail.com', '1-5', segmentosEnsino[0].segmento)
aluno6 = Aluno('aluno1-6', '1-6', '1-6', '1-6', 'aluno1-6', 'aluno1-6@gmail.com', 'aluno1-6', 'Sim', turma1, '', 'pai1-6@gmail.com', '1-6', segmentosEnsino[0].segmento)
aluno7 = Aluno('aluno1-7', '1-7', '1-7', '1-7', 'aluno1-7', 'aluno1-7@gmail.com', 'aluno1-7', 'Sim', turma1, '', 'pai1-7@gmail.com', '1-7', segmentosEnsino[0].segmento)
aluno8 = Aluno('aluno1-8', '1-8', '1-8', '1-8', 'aluno1-8', 'aluno1-8@gmail.com', 'aluno1-8', 'Sim', turma1, '', 'pai1-8@gmail.com', '1-8', segmentosEnsino[0].segmento)
aluno9 = Aluno('aluno1-9', '1-9', '1-9', '1-9', 'aluno1-9', 'aluno1-9@gmail.com', 'aluno1-9', 'Sim', turma1, '', 'pai1-9@gmail.com', '1-9', segmentosEnsino[0].segmento)
aluno10 = Aluno('aluno1-10', '1-10', '1-10', '1-10', 'aluno1-10', 'aluno1-10@gmail.com', 'aluno1-10', 'Sim', turma1, '', 'pai1-10@gmail.com', '1-10', segmentosEnsino[0].segmento)
alunos1 = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]
professor1 = Professor('professor1-1', '1-1', '1-1', '1-1', 'professor1-1', 'professor1-1@gmail.com', 'professor1-1', 'Sim', turma1, '1-1', [], segmentosEnsino[0].segmento)


turma2 = Turma('turma2', segmentosEnsino[0].segmento, segmentosEnsino[0].cursos[1], '2024', [], [], [], 'Sim')
aluno11 = Aluno('aluno2-11', '2-11', '2-11', '2-11', 'aluno2-11', 'aluno2-11@gmail.com', 'aluno2-11', 'Sim', turma2, '', 'pai2-11@gmail.com', '2-11', segmentosEnsino[0].segmento) 
aluno12 = Aluno('aluno2-12', '2-12', '2-12', '2-12', 'aluno2-12', 'aluno2-12@gmail.com', 'aluno2-12', 'Sim', turma2, '', 'pai2-12@gmail.com', '2-12', segmentosEnsino[0].segmento)
aluno13 = Aluno('aluno2-13', '2-13', '2-13', '2-13', 'aluno2-13', 'aluno2-13@gmail.com', 'aluno2-13', 'Sim', turma2, '', 'pai2-13@gmail.com', '2-13', segmentosEnsino[0].segmento)
aluno14 = Aluno('aluno2-14', '2-14', '2-14', '2-14', 'aluno2-14', 'aluno2-14@gmail.com', 'aluno2-14', 'Sim', turma2, '', 'pai2-14@gmail.com', '2-14', segmentosEnsino[0].segmento)
aluno15 = Aluno('aluno2-15', '2-15', '2-15', '2-15', 'aluno2-15', 'aluno2-15@gmail.com', 'aluno2-15', 'Sim', turma2, '', 'pai2-15@gmail.com', '2-15', segmentosEnsino[0].segmento)
aluno16 = Aluno('aluno2-16', '2-16', '2-16', '2-16', 'aluno2-16', 'aluno2-16@gmail.com', 'aluno2-16', 'Sim', turma2, '', 'pai2-16@gmail.com', '2-16', segmentosEnsino[0].segmento)
aluno17 = Aluno('aluno2-17', '2-17', '2-17', '2-17', 'aluno2-17', 'aluno2-17@gmail.com', 'aluno2-17', 'Sim', turma2, '', 'pai2-17@gmail.com', '2-17', segmentosEnsino[0].segmento)
aluno18 = Aluno('aluno2-18', '2-18', '2-18', '2-18', 'aluno2-18', 'aluno2-18@gmail.com', 'aluno2-18', 'Sim', turma2, '', 'pai2-18@gmail.com', '2-18', segmentosEnsino[0].segmento)
aluno19 = Aluno('aluno2-19', '2-19', '2-19', '2-19', 'aluno2-19', 'aluno2-19@gmail.com', 'aluno2-19', 'Sim', turma2, '', 'pai2-19@gmail.com', '2-19', segmentosEnsino[0].segmento)
aluno20 = Aluno('aluno2-20', '2-20', '2-20', '2-20', 'aluno2-20', 'aluno2-20@gmail.com', 'aluno2-20', 'Sim', turma2, '', 'pai2-20@gmail.com', '2-20', segmentosEnsino[0].segmento)
alunos2 = [aluno11, aluno12, aluno13, aluno14, aluno15, aluno16, aluno17, aluno18, aluno19, aluno20]
professor2 = Professor('professor1-2', '1-2', '1-2', '1-2', 'professor1-2', 'professor1-2@gmail.com', 'professor1-2', 'Sim', turma2, '1-2', [], segmentosEnsino[0].segmento)


turma3 = Turma('turma3', segmentosEnsino[0].segmento, segmentosEnsino[0].cursos[2], '2024', [], [], [], 'Sim')
aluno21 = Aluno('aluno3-31', '3-31', '3-31', '3-31', 'aluno3-31', 'aluno3-31@gmail.com', 'aluno3-31', 'Sim', turma3, '', 'pai3-31@gmail.com', '3-31', segmentosEnsino[0].segmento)
aluno22 = Aluno('aluno3-32', '3-32', '3-32', '3-32', 'aluno3-32', 'aluno3-32@gmail.com', 'aluno3-32', 'Sim', turma3, '', 'pai3-32@gmail.com', '3-32', segmentosEnsino[0].segmento)
aluno23 = Aluno('aluno3-33', '3-33', '3-33', '3-33', 'aluno3-33', 'aluno3-33@gmail.com', 'aluno3-33', 'Sim', turma3, '', 'pai3-33@gmail.com', '3-33', segmentosEnsino[0].segmento)
aluno24 = Aluno('aluno3-34', '3-34', '3-34', '3-34', 'aluno3-34', 'aluno3-34@gmail.com', 'aluno3-34', 'Sim', turma3, '', 'pai3-34@gmail.com', '3-34', segmentosEnsino[0].segmento)
aluno25 = Aluno('aluno3-35', '3-35', '3-35', '3-35', 'aluno3-35', 'aluno3-35@gmail.com', 'aluno3-35', 'Sim', turma3, '', 'pai3-35@gmail.com', '3-35', segmentosEnsino[0].segmento)
aluno26 = Aluno('aluno3-36', '3-36', '3-36', '3-36', 'aluno3-36', 'aluno3-36@gmail.com', 'aluno3-36', 'Sim', turma3, '', 'pai3-36@gmail.com', '3-36', segmentosEnsino[0].segmento)
aluno27 = Aluno('aluno3-37', '3-37', '3-37', '3-37', 'aluno3-37', 'aluno3-37@gmail.com', 'aluno3-37', 'Sim', turma3, '', 'pai3-37@gmail.com', '3-37', segmentosEnsino[0].segmento)
aluno28 = Aluno('aluno3-38', '3-38', '3-38', '3-38', 'aluno3-38', 'aluno3-38@gmail.com', 'aluno3-38', 'Sim', turma3, '', 'pai3-38@gmail.com', '3-38', segmentosEnsino[0].segmento)
aluno29 = Aluno('aluno3-39', '3-39', '3-39', '3-39', 'aluno3-39', 'aluno3-39@gmail.com', 'aluno3-39', 'Sim', turma3, '', 'pai3-39@gmail.com', '3-39', segmentosEnsino[0].segmento)
aluno30 = Aluno('aluno3-40', '3-40', '3-40', '3-40', 'aluno3-40', 'aluno3-40@gmail.com', 'aluno3-40', 'Sim', turma3, '', 'pai3-40@gmail.com', '3-40', segmentosEnsino[0].segmento)
alunos3 = [aluno21, aluno22, aluno23, aluno24, aluno25, aluno26, aluno27, aluno28, aluno29, aluno30]
professor3 = Professor('professor1-3', '1-3', '1-3', '1-3', 'professor1-3', 'professor1-3@gmail.com', 'professor1-3', 'Sim', turma3, '1-3', [], segmentosEnsino[0].segmento)


turma4 = Turma('turma4', segmentosEnsino[1].segmento, segmentosEnsino[1].cursos[0], '2024', [], [], [], 'Sim')
aluno31 = Aluno('aluno4-41', '4-41', '4-41', '4-41', 'aluno4-41', 'aluno4-41@gmail.com', 'aluno4-41', 'Sim', turma4, '', 'pai4-41@gmail.com', '4-41', segmentosEnsino[1].segmento)
aluno32 = Aluno('aluno4-42', '4-42', '4-42', '4-42', 'aluno4-42', 'aluno4-42@gmail.com', 'aluno4-42', 'Sim', turma4, '', 'pai4-42@gmail.com', '4-42', segmentosEnsino[1].segmento)
aluno33 = Aluno('aluno4-43', '4-43', '4-43', '4-43', 'aluno4-43', 'aluno4-43@gmail.com', 'aluno4-43', 'Sim', turma4, '', 'pai4-43@gmail.com', '4-43', segmentosEnsino[1].segmento)
aluno34 = Aluno('aluno4-44', '4-44', '4-44', '4-44', 'aluno4-44', 'aluno4-44@gmail.com', 'aluno4-44', 'Sim', turma4, '', 'pai4-44@gmail.com', '4-44', segmentosEnsino[1].segmento)
aluno35 = Aluno('aluno4-45', '4-45', '4-45', '4-45', 'aluno4-45', 'aluno4-45@gmail.com', 'aluno4-45', 'Sim', turma4, '', 'pai4-45@gmail.com', '4-45', segmentosEnsino[1].segmento)
aluno36 = Aluno('aluno4-46', '4-46', '4-46', '4-46', 'aluno4-46', 'aluno4-46@gmail.com', 'aluno4-46', 'Sim', turma4, '', 'pai4-46@gmail.com', '4-46', segmentosEnsino[1].segmento)
aluno37 = Aluno('aluno4-47', '4-47', '4-47', '4-47', 'aluno4-47', 'aluno4-47@gmail.com', 'aluno4-47', 'Sim', turma4, '', 'pai4-47@gmail.com', '4-47', segmentosEnsino[1].segmento)
aluno38 = Aluno('aluno4-48', '4-48', '4-48', '4-48', 'aluno4-48', 'aluno4-48@gmail.com', 'aluno4-48', 'Sim', turma4, '', 'pai4-48@gmail.com', '4-48', segmentosEnsino[1].segmento)
aluno39 = Aluno('aluno4-49', '4-49', '4-49', '4-49', 'aluno4-49', 'aluno4-49@gmail.com', 'aluno4-49', 'Sim', turma4, '', 'pai4-49@gmail.com', '4-49', segmentosEnsino[1].segmento)
aluno40 = Aluno('aluno4-50', '4-50', '4-50', '4-50', 'aluno4-50', 'aluno4-50@gmail.com', 'aluno4-50', 'Sim', turma4, '', 'pai4-50@gmail.com', '4-50', segmentosEnsino[1].segmento)
alunos4 = [aluno31, aluno32, aluno33, aluno34, aluno35, aluno36, aluno37, aluno38, aluno39, aluno40]
professor4 = Professor('professor1-4', '1-4', '1-4', '1-4', 'professor1-4', 'professor1-4@gmail.com', 'professor1-4', 'Sim', turma4, '1-4', [], segmentosEnsino[1].segmento)


turma5 = Turma('turma5', segmentosEnsino[1].segmento, segmentosEnsino[1].cursos[1], '2024', [], [], [], 'Sim')
aluno41 = Aluno('aluno5-51', '5-51', '5-51', '5-51', 'aluno5-51', 'aluno5-51@gmail.com', 'aluno5-51', 'Sim', turma5, '', 'pai5-51@gmail.com', '5-51', segmentosEnsino[1].segmento)
aluno42 = Aluno('aluno5-52', '5-52', '5-52', '5-52', 'aluno5-52', 'aluno5-52@gmail.com', 'aluno5-52', 'Sim', turma5, '', 'pai5-52@gmail.com', '5-52', segmentosEnsino[1].segmento)
aluno43 = Aluno('aluno5-53', '5-53', '5-53', '5-53', 'aluno5-53', 'aluno5-53@gmail.com', 'aluno5-53', 'Sim', turma5, '', 'pai5-53@gmail.com', '5-53', segmentosEnsino[1].segmento)
aluno44 = Aluno('aluno5-54', '5-54', '5-54', '5-54', 'aluno5-54', 'aluno5-54@gmail.com', 'aluno5-54', 'Sim', turma5, '', 'pai5-54@gmail.com', '5-54', segmentosEnsino[1].segmento)
aluno45 = Aluno('aluno5-55', '5-55', '5-55', '5-55', 'aluno5-55', 'aluno5-55@gmail.com', 'aluno5-55', 'Sim', turma5, '', 'pai5-55@gmail.com', '5-55', segmentosEnsino[1].segmento)
aluno46 = Aluno('aluno5-56', '5-56', '5-56', '5-56', 'aluno5-56', 'aluno5-56@gmail.com', 'aluno5-56', 'Sim', turma5, '', 'pai5-56@gmail.com', '5-56', segmentosEnsino[1].segmento)
aluno47 = Aluno('aluno5-57', '5-57', '5-57', '5-57', 'aluno5-57', 'aluno5-57@gmail.com', 'aluno5-57', 'Sim', turma5, '', 'pai5-57@gmail.com', '5-57', segmentosEnsino[1].segmento)
aluno48 = Aluno('aluno5-58', '5-58', '5-58', '5-58', 'aluno5-58', 'aluno5-58@gmail.com', 'aluno5-58', 'Sim', turma5, '', 'pai5-58@gmail.com', '5-58', segmentosEnsino[1].segmento)
aluno49 = Aluno('aluno5-59', '5-59', '5-59', '5-59', 'aluno5-59', 'aluno5-59@gmail.com', 'aluno5-59', 'Sim', turma5, '', 'pai5-59@gmail.com', '5-59', segmentosEnsino[1].segmento)
aluno50 = Aluno('aluno5-60', '5-60', '5-60', '5-60', 'aluno5-60', 'aluno5-60@gmail.com', 'aluno5-60', 'Sim', turma5, '', 'pai5-60@gmail.com', '5-60', segmentosEnsino[1].segmento)
alunos5 = [aluno41, aluno42, aluno43, aluno44, aluno45, aluno46, aluno47, aluno48, aluno49, aluno50]
professor5 = Professor('professor1-5', '1-5', '1-5', '1-5', 'professor1-5', 'professor1-5@gmail.com', 'professor1-5', 'Sim', turma5, '1-5', [], segmentosEnsino[1].segmento)

professores = [professor1, professor2, professor3, professor4, professor5]

disciplina1 = Disciplinas(1, '1-1', segmentosEnsino[0].segmento, professores[0], 'Sim')
disciplina2 = Disciplinas(2, '1-2', segmentosEnsino[0].segmento, professores[1], 'Sim')
disciplina3 = Disciplinas(3, '1-3', segmentosEnsino[0].segmento, professores[2], 'Sim')
disciplina4 = Disciplinas(4, '1-4', segmentosEnsino[1].segmento, professores[3], 'Sim')
disciplina5 = Disciplinas(5, '1-5', segmentosEnsino[1].segmento, professores[4], 'Sim')

alunos = [alunos1, alunos2, alunos3, alunos4, alunos5]
disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]
turmas = [turma1, turma2, turma3, turma4, turma5]

for i in range(len(professores)):
    professores[i].disciplinas.append(disciplinas[i])

for i in range(len(turmas)):
    for j in range(len(alunos[i])):
        turmas[i].alunos.append(alunos[i][j])
    turmas[i].professores.append(professores[i])
    turmas[i].disciplinas.append(disciplinas[i])

#FUNÇÕES ==================================================================================================================================================================

# TURMAS ==================================================================================================================================================================
def imprimirTurma(turma):
    print(turmas[turma])
    return

#===========================================================================
def inserirTurma():
    print('Insira as seguintes informações:')
    nome = input('Nome: ')
    segmentoEnsino = input('Segmento de Ensino: ')
    opcaoCurso = input('Opção de Curso: ')
    anoEscolar = input('Ano Escolar: ')
    alunosY = []
    while True:
        try:
            alunosX = int(input('Quantidade de Alunos:'))
            for i in range(alunosX):
                x = 0
                nomeX = input('Insira o nome do Estudante: ')
                for j in range(len(alunos)):
                    for k in range(len(alunos[j])):
                        if nomeX == alunos[j][k].nome:
                            alunosY.append(alunos[j][k])
                            print('Aluno existente!')
                            x += 1
                if x == 0:
                    print('Aluno Inexistente!')
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue
    
    professoresY = []
    while True:
        try:
            professoresX = int(input('Quantidade de Professores: '))
            for i in range(professoresX):
                x = 0
                nomeX = input('Insira o nome do Professor: ')
                for j in range(len(professores)):
                    if nomeX == professores[j].nome:
                        professoresY.append(professores[j])
                        print('Professor existente!')
                        x += 1
                if x == 0:
                    print('Professor Inexistente!')
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue

    disciplinasY = []
    while True:
        try:
            disciplinasX = int(input('Quantidade de Disciplinas: '))
            for i in range(disciplinasX):
                x = 0
                idX = int(input('Insira o id da Disciplina: '))
                for j in range(len(disciplinas)):
                    if idX == disciplinas[j].id:
                        disciplinasY.append(disciplinas[j])
                        print('Disciplina existente!')
                        x += 1
                if x == 0:
                    print('Disciplina Inexistente!')
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue
    
    turmaX = Turma(nome, segmentoEnsino, opcaoCurso, anoEscolar, alunosY, professoresY, disciplinasY)
    turmas.append(turmaX)
    print(turmaX)

    return

#===========================================================================
def editarTurma(turma):
    print('o que você deseja editar?')
    print('''
Nome
Segmento de Ensino
Opção de Curso
Ano Escolar
Alunos
Professores
Disciplinas
sair
''')
    opcaoX = input()

    if opcaoX.upper() == 'NOME':
        nomeX = input('Insira o novo nome:')
        turmas[turma].nome = nomeX
        print(f'Nome alterado para: {nomeX}')
        return
    
    elif opcaoX.upper() == 'SEGMENTO DE ENSINO':
        if turmas[turma].segmentoEnsino.upper() == 'ENSINO MEDIO':
            turmas[turma].segmentoEnsino = segmentosEnsino[1].segmento
            print(f'Segmento de Ensino alterado para: {turmas[turma].segmentoEnsino}')
        elif turmas[turma].segmentoEnsino.upper() == 'ENSINO SUPERIOR':
            turmas[turma].segmentoEnsino = segmentosEnsino[0].segmento
            print(f'Segmento de Ensino alterado para: {turmas[turma].segmentoEnsino}')
        return
    
    elif opcaoX.upper() == 'OPÇÃO DE CURSO':
        print('Escolha uma das opções abaixo:')
        if turmas[turma].segmentoEnsino.upper() == 'ENSINO MEDIO':
            for i in range(len(segmentosEnsino[0].cursos)):
                print(f'{i+1}ª opção: {segmentosEnsino[0].cursos}')
            escolha = int(input())
            turmas[turma].opcaoCurso = segmentosEnsino[0].cursos[escolha-1]
            print(f'Opção de curso alterada para: {segmentosEnsino[0].cursos[escolha-1]}')
        elif turmas[turma].segmentoEnsino.upper() == 'ENSINO SUPERIOR':
            for i in range(len(segmentosEnsino[1].cursos)):
                print(f'{i+1}ª opção: {segmentosEnsino[1].cursos}')
            escolha = int(input())
            turmas[turma].opcaoCurso = segmentosEnsino[1].cursos[escolha-1]
            print(f'Opção de curso alterada para: {segmentosEnsino[0].cursos[escolha-1]}')
        return
    
    elif opcaoX.upper() == 'ANO ESCOLAR':
        anoEscolarX = input('Insira um novo Ano Escolar:')
        turmas[turma].anoEscolar = anoEscolarX
        print(f'Ano Escolar alterado para: {anoEscolarX}')
        return
    
    elif opcaoX.upper() == 'ALUNOS': 
        escolha = input('Você deseja remover ou adicionar um estudante? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            alunoX = input('Insira o aluno que você deseja alterar: ')
            for i in range(len(turmas[turma].alunos)):
                print(i)
                if alunoX == turmas[turma].alunos[i].nome:
                    print(f'Aluno {turmas[turma].alunos[i].nome} removido!')
                    turmas[turma].alunos.pop(i)
                    x += 1
                    break
            if x == 0:
                print(f'O Aluno {alunoX} é inexistente!')
        elif escolha.upper() == 'ADICIONAR':
            x = 0
            alunoX = input('Insira o aluno que você deseja alterar: ')
            for i in range(len(alunos)):
                for j in range(len(alunos[i])):
                    if alunoX == alunos[i][j].nome:
                        print(f'Aluno {alunos[i][j].nome} adicionado!')
                        turmas[turma].alunos.append(alunos[i][j])
                        x += 1
            if x == 0:
                print(f'O luno {alunoX} é inexistente!')
        return
    
    elif opcaoX.upper() == 'PROFESSORES':
        escolha = input('Você deseja remover ou adicionar um Professor? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            professorX = input('Insira o Professor que você deseja remover: ')
            for i in range(len(turmas[turma].professores)):
                if professorX == turmas[turma].professores[i].nome:
                    print(f'Professor {turmas[turma].professores[i].nome} removido!')
                    turmas[turma].professores.pop(i)
                    x += 1
                    break
            if x == 0:
                print(f'O Professor {professorX} é inexistente!')
        elif escolha.upper() == 'ADICIONAR':
            x = 0
            professorX = input('Insira o Professor que você deseja adicionar: ')
            for i in range(len(professores)):
                if professorX == professores[i].nome:
                    print(f'Professor {professores[i].nome} adicionado!')
                    turmas[turma].professores.append(professores[i])
                    x += 1
            if x == 0:
                print(f'O Professor {professorX} é inexistente!')
        return

    elif opcaoX.upper() == 'DISCIPLINAS':
        escolha = input('Você deseja remover ou adicionar uma Disciplina? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            disciplinaX = int(input('Insira o ID da Disciplina que você deseja remover: '))
            for i in range(len(turmas[turma].disciplinas)):
                if disciplinaX == turmas[turma].disciplinas[i].id:
                    print(f'Disciplina {turmas[turma].disciplinas[i].id} removida!')
                    turmas[turma].disciplinas.pop(i)
                    x += 1
                    break
            if x == 0:
                print(f'A Disciplina {disciplinaX} é inexistente!')
        elif escolha.upper() == 'ADICIONAR':
            x = 0
            disciplinaX = input('Insira o ID da Disciplina que você deseja adicionar: ')
            for i in range(len(disciplinas)):
                if disciplinaX == disciplinas[i].id:
                    print(f'Disciplina {disciplinas[i].id} adicionado!')
                    turmas[turma].disciplinas.append(disciplinas[i])
                    x += 1
            if x == 0:
                print(f'A Disciplina {disciplinaX} é inexistente!')
        return
                
    elif opcaoX.upper() == 'SAIR':
        return
    else:
        print('Opção Inválida!')

    return

#===========================================================================
def desativarTurma(turma):
    opcaoX = input('Você tem certeza de que deseja desativar a turma? ')
    if opcaoX.upper() == 'SIM':
        turmas[turma].ativo = 'Não'
        print(f'Turma {turmas[turma].nome} desativada!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    return

#===========================================================================
def excluirTurma(turma):
    opcaoX = input('Você tem certeza de que deseja excluir a turma? ')
    if opcaoX.upper() == 'SIM':
        turmas.remove(turmas[turma])
        print('Turma excluída!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    return

#===========================================================================
def crudTurma():
    print('O que fazer com a turma?')
    print('''
Imprimir
Inserir
Editar
Desativar
Excluir
sair
''')
    opcao = input()

    if opcao.upper() == 'INSERIR':
        return inserirTurma()
    else:
        print('qual turma acessar?')
        for i in range(len(turmas)):
            print(f'{i+1}º turma: {turmas[i].nome}')
        escolha = int(input())-1
    
    if opcao.upper() == 'IMPRIMIR':
        return imprimirTurma(escolha)
    elif opcao.upper() == 'EDITAR':
        return editarTurma(escolha)
    elif opcao.upper() == 'DESATIVAR':
        return desativarTurma(escolha)
    elif opcao.upper() == 'EXCLUIR':
        return excluirTurma(escolha)
    elif opcao.upper() == 'SAIR':
        return
    else:
        print('Opção Inválida!')

    return

#DISCIPLINAS ==================================================================================================================================================================
def crudDisciplina():
    return

#PROFESSORES ==================================================================================================================================================================
def crudProfessor():
    return

#ESTUDANTES ==================================================================================================================================================================
def crudEstudante():
    return

#PARTE PRÁTICA ==================================================================================================================================================================

"""
1. mecatrônica, eletromecânica e informática. Obrigatoriamente, um aluno do EM deve estar associado a uma dessas opções; fechou ================
2. O aluno do EM pode solicitar transferência para outra opção de curso durante a sua vida acadêmica na instituição;
4. O aluno do ensino superior poderá cursar os dois segmentos paralelamente;
5. Caso o aluno tenha optado por apenas curso (ciências da computação ou pedagogia), é permitido ao aluno transferir de curso durante a sua vida acadêmica na instituição;
6. É possível imprimir, inserir, editar, desativar e excluir uma turma.
11. É possível inserir, editar, desativar e excluir uma disciplina;
13. É possível inserir, editar, desativar e excluir um professor;
15. É possível inserir, editar, desativar e excluir um estudante.
filiação é o nome do pai e da mãe
"""

print('Bem vindo ao sistema estudantil!')
x = 0
while x == 0:
    print('O que você deseja fazer? ')
    print('''
Acessar turmas
Acessar disciplinas
Acessar professores
Acessar estudantes
sair
''')
    opcao = input('')
    if opcao.upper() == 'TURMAS':
        crudTurma()
        continue
    elif opcao.upper() == 'DISCIPLINAS':
        continue
    elif opcao.upper() == 'PROFESSORES':
        continue
    elif opcao.upper() == 'ESTUDANTES':
        continue
    elif opcao.upper() == 'SAIR':
        break
    else:
        print('Foi inseirdo uma opção inválida: ')
        continue