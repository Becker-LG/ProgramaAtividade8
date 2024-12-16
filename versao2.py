from classes import Aluno
from classes import Professor
from classes import SegmentoEnsino
from classes import Turma
from classes import Disciplina

#CRIAÇÃO DOS OBJETOS ==================================================================================================================================================================

segmentoEnsino1 = SegmentoEnsino('Ensino Medio', ['Mecatrônica', 'Eletromecânica', 'Informática'], 'Sim')
segmentoEnsino2 = SegmentoEnsino('Ensino Superior', ['Ciências da Computação', 'Pedagogia'], 'Sim')
segmentosEnsino = [segmentoEnsino1, segmentoEnsino2]
print(segmentosEnsino[0].cursos)
print(segmentosEnsino[1].cursos)

turma1 = Turma('turma1', segmentosEnsino[0].segmento, segmentosEnsino[0].cursos[0], '2024', [], [], [], 'Sim')

aluno1 = Aluno('aluno1-1', '1-1', '1-1', '1-1', 'aluno1-1', 'aluno1-1@gmail.com', 'aluno1-1', 'Sim', [turma1], ['pai1-1', 'mãe1-1'], 'pai1-1@gmail.com', '1-1', segmentosEnsino[0].segmento)
aluno2 = Aluno('aluno1-2', '1-2', '1-2', '1-2', 'aluno1-2', 'aluno1-2@gmail.com', 'aluno1-2', 'Sim', [turma1], ['pai1-2', 'mãe1-2'], 'pai1-2@gmail.com', '1-2', segmentosEnsino[0].segmento)
aluno3 = Aluno('aluno1-3', '1-3', '1-3', '1-3', 'aluno1-3', 'aluno1-3@gmail.com', 'aluno1-3', 'Sim', [turma1], ['pai1-3', 'mãe1-3'], 'pai1-3@gmail.com', '1-3', segmentosEnsino[0].segmento)
aluno4 = Aluno('aluno1-4', '1-4', '1-4', '1-4', 'aluno1-4', 'aluno1-4@gmail.com', 'aluno1-4', 'Sim', [turma1], ['pai1-4', 'mãe1-4'], 'pai1-4@gmail.com', '1-4', segmentosEnsino[0].segmento)
aluno5 = Aluno('aluno1-5', '1-5', '1-5', '1-5', 'aluno1-5', 'aluno1-5@gmail.com', 'aluno1-5', 'Sim', [turma1], ['pai1-5', 'mãe1-5'], 'pai1-5@gmail.com', '1-5', segmentosEnsino[0].segmento)
aluno6 = Aluno('aluno1-6', '1-6', '1-6', '1-6', 'aluno1-6', 'aluno1-6@gmail.com', 'aluno1-6', 'Sim', [turma1], ['pai1-6', 'mãe1-6'], 'pai1-6@gmail.com', '1-6', segmentosEnsino[0].segmento)
aluno7 = Aluno('aluno1-7', '1-7', '1-7', '1-7', 'aluno1-7', 'aluno1-7@gmail.com', 'aluno1-7', 'Sim', [turma1], ['pai1-7', 'mãe1-7'], 'pai1-7@gmail.com', '1-7', segmentosEnsino[0].segmento)
aluno8 = Aluno('aluno1-8', '1-8', '1-8', '1-8', 'aluno1-8', 'aluno1-8@gmail.com', 'aluno1-8', 'Sim', [turma1], ['pai1-8', 'mãe1-8'], 'pai1-8@gmail.com', '1-8', segmentosEnsino[0].segmento)
aluno9 = Aluno('aluno1-9', '1-9', '1-9', '1-9', 'aluno1-9', 'aluno1-9@gmail.com', 'aluno1-9', 'Sim', [turma1], ['pai1-9', 'mãe1-9'], 'pai1-9@gmail.com', '1-9', segmentosEnsino[0].segmento)
aluno10 = Aluno('aluno1-10', '1-10', '1-10', '1-10', 'aluno1-10', 'aluno1-10@gmail.com', 'aluno1-10', 'Sim', [turma1], ['pai1-10', 'mãe1-10'], 'pai1-10@gmail.com', '1-10', segmentosEnsino[0].segmento)
alunos1 = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]
professor1 = Professor('professor1-1', '1-1', '1-1', '1-1', 'professor1-1', 'professor1-1@gmail.com', 'professor1-1', 'Sim', [], '1-1', [], [])


turma2 = Turma('turma2', segmentosEnsino[0].segmento, segmentosEnsino[0].cursos[1], '2024', [], [], [], 'Sim')
aluno11 = Aluno('aluno2-11', '2-11', '2-11', '2-11', 'aluno2-11', 'aluno2-11@gmail.com', 'aluno2-11', 'Sim', [turma2], ['pai2-11', 'mãe2-11'], 'pai2-11@gmail.com', '2-11', segmentosEnsino[0].segmento) 
aluno12 = Aluno('aluno2-12', '2-12', '2-12', '2-12', 'aluno2-12', 'aluno2-12@gmail.com', 'aluno2-12', 'Sim', [turma2], ['pai2-12', 'mãe2-12'], 'pai2-12@gmail.com', '2-12', segmentosEnsino[0].segmento)
aluno13 = Aluno('aluno2-13', '2-13', '2-13', '2-13', 'aluno2-13', 'aluno2-13@gmail.com', 'aluno2-13', 'Sim', [turma2], ['pai2-13', 'mãe2-13'], 'pai2-13@gmail.com', '2-13', segmentosEnsino[0].segmento)
aluno14 = Aluno('aluno2-14', '2-14', '2-14', '2-14', 'aluno2-14', 'aluno2-14@gmail.com', 'aluno2-14', 'Sim', [turma2], ['pai2-14', 'mãe2-14'], 'pai2-14@gmail.com', '2-14', segmentosEnsino[0].segmento)
aluno15 = Aluno('aluno2-15', '2-15', '2-15', '2-15', 'aluno2-15', 'aluno2-15@gmail.com', 'aluno2-15', 'Sim', [turma2], ['pai2-15', 'mãe2-15'], 'pai2-15@gmail.com', '2-15', segmentosEnsino[0].segmento)
aluno16 = Aluno('aluno2-16', '2-16', '2-16', '2-16', 'aluno2-16', 'aluno2-16@gmail.com', 'aluno2-16', 'Sim', [turma2], ['pai2-16', 'mãe2-16'], 'pai2-16@gmail.com', '2-16', segmentosEnsino[0].segmento)
aluno17 = Aluno('aluno2-17', '2-17', '2-17', '2-17', 'aluno2-17', 'aluno2-17@gmail.com', 'aluno2-17', 'Sim', [turma2], ['pai2-17', 'mãe2-17'], 'pai2-17@gmail.com', '2-17', segmentosEnsino[0].segmento)
aluno18 = Aluno('aluno2-18', '2-18', '2-18', '2-18', 'aluno2-18', 'aluno2-18@gmail.com', 'aluno2-18', 'Sim', [turma2], ['pai2-18', 'mãe2-18'], 'pai2-18@gmail.com', '2-18', segmentosEnsino[0].segmento)
aluno19 = Aluno('aluno2-19', '2-19', '2-19', '2-19', 'aluno2-19', 'aluno2-19@gmail.com', 'aluno2-19', 'Sim', [turma2], ['pai2-19', 'mãe2-19'], 'pai2-19@gmail.com', '2-19', segmentosEnsino[0].segmento)
aluno20 = Aluno('aluno2-20', '2-20', '2-20', '2-20', 'aluno2-20', 'aluno2-20@gmail.com', 'aluno2-20', 'Sim', [turma2], ['pai2-20', 'mãe2-20'], 'pai2-20@gmail.com', '2-20', segmentosEnsino[0].segmento)
alunos2 = [aluno11, aluno12, aluno13, aluno14, aluno15, aluno16, aluno17, aluno18, aluno19, aluno20]
professor2 = Professor('professor1-2', '1-2', '1-2', '1-2', 'professor1-2', 'professor1-2@gmail.com', 'professor1-2', 'Sim', [], '1-2', [], [])


turma3 = Turma('turma3', segmentosEnsino[0].segmento, segmentosEnsino[0].cursos[2], '2024', [], [], [], 'Sim')
aluno21 = Aluno('aluno3-31', '3-31', '3-31', '3-31', 'aluno3-31', 'aluno3-31@gmail.com', 'aluno3-31', 'Sim', [turma3], ['pai3-31', 'mãe3-31'], 'pai3-31@gmail.com', '3-31', segmentosEnsino[0].segmento)
aluno22 = Aluno('aluno3-32', '3-32', '3-32', '3-32', 'aluno3-32', 'aluno3-32@gmail.com', 'aluno3-32', 'Sim', [turma3], ['pai3-32', 'mãe3-32'], 'pai3-32@gmail.com', '3-32', segmentosEnsino[0].segmento)
aluno23 = Aluno('aluno3-33', '3-33', '3-33', '3-33', 'aluno3-33', 'aluno3-33@gmail.com', 'aluno3-33', 'Sim', [turma3], ['pai3-33', 'mãe3-33'], 'pai3-33@gmail.com', '3-33', segmentosEnsino[0].segmento)
aluno24 = Aluno('aluno3-34', '3-34', '3-34', '3-34', 'aluno3-34', 'aluno3-34@gmail.com', 'aluno3-34', 'Sim', [turma3], ['pai3-34', 'mãe3-34'], 'pai3-34@gmail.com', '3-34', segmentosEnsino[0].segmento)
aluno25 = Aluno('aluno3-35', '3-35', '3-35', '3-35', 'aluno3-35', 'aluno3-35@gmail.com', 'aluno3-35', 'Sim', [turma3], ['pai3-35', 'mãe3-35'], 'pai3-35@gmail.com', '3-35', segmentosEnsino[0].segmento)
aluno26 = Aluno('aluno3-36', '3-36', '3-36', '3-36', 'aluno3-36', 'aluno3-36@gmail.com', 'aluno3-36', 'Sim', [turma3], ['pai3-36', 'mãe3-36'], 'pai3-36@gmail.com', '3-36', segmentosEnsino[0].segmento)
aluno27 = Aluno('aluno3-37', '3-37', '3-37', '3-37', 'aluno3-37', 'aluno3-37@gmail.com', 'aluno3-37', 'Sim', [turma3], ['pai3-37', 'mãe3-37'], 'pai3-37@gmail.com', '3-37', segmentosEnsino[0].segmento)
aluno28 = Aluno('aluno3-38', '3-38', '3-38', '3-38', 'aluno3-38', 'aluno3-38@gmail.com', 'aluno3-38', 'Sim', [turma3], ['pai3-38', 'mãe3-38'], 'pai3-38@gmail.com', '3-38', segmentosEnsino[0].segmento)
aluno29 = Aluno('aluno3-39', '3-39', '3-39', '3-39', 'aluno3-39', 'aluno3-39@gmail.com', 'aluno3-39', 'Sim', [turma3], ['pai3-39', 'mãe3-39'], 'pai3-39@gmail.com', '3-39', segmentosEnsino[0].segmento)
aluno30 = Aluno('aluno3-40', '3-40', '3-40', '3-40', 'aluno3-40', 'aluno3-40@gmail.com', 'aluno3-40', 'Sim', [turma3], ['pai3-40', 'mãe3-40'], 'pai3-40@gmail.com', '3-40', segmentosEnsino[0].segmento)
alunos3 = [aluno21, aluno22, aluno23, aluno24, aluno25, aluno26, aluno27, aluno28, aluno29, aluno30]
professor3 = Professor('professor1-3', '1-3', '1-3', '1-3', 'professor1-3', 'professor1-3@gmail.com', 'professor1-3', 'Sim', [], '1-3', [], [])


turma4 = Turma('turma4', segmentosEnsino[1].segmento, segmentosEnsino[1].cursos[0], '2024', [], [], [], 'Sim')
aluno31 = Aluno('aluno4-41', '4-41', '4-41', '4-41', 'aluno4-41', 'aluno4-41@gmail.com', 'aluno4-41', 'Sim', [turma4], ['pai4-41', 'mãe4-41'], 'pai4-41@gmail.com', '4-41', segmentosEnsino[1].segmento)
aluno32 = Aluno('aluno4-42', '4-42', '4-42', '4-42', 'aluno4-42', 'aluno4-42@gmail.com', 'aluno4-42', 'Sim', [turma4], ['pai4-42', 'mãe4-42'], 'pai4-42@gmail.com', '4-42', segmentosEnsino[1].segmento)
aluno33 = Aluno('aluno4-43', '4-43', '4-43', '4-43', 'aluno4-43', 'aluno4-43@gmail.com', 'aluno4-43', 'Sim', [turma4], ['pai4-43', 'mãe4-43'], 'pai4-43@gmail.com', '4-43', segmentosEnsino[1].segmento)
aluno34 = Aluno('aluno4-44', '4-44', '4-44', '4-44', 'aluno4-44', 'aluno4-44@gmail.com', 'aluno4-44', 'Sim', [turma4], ['pai4-44', 'mãe4-44'], 'pai4-44@gmail.com', '4-44', segmentosEnsino[1].segmento)
aluno35 = Aluno('aluno4-45', '4-45', '4-45', '4-45', 'aluno4-45', 'aluno4-45@gmail.com', 'aluno4-45', 'Sim', [turma4], ['pai4-45', 'mãe4-45'], 'pai4-45@gmail.com', '4-45', segmentosEnsino[1].segmento)
aluno36 = Aluno('aluno4-46', '4-46', '4-46', '4-46', 'aluno4-46', 'aluno4-46@gmail.com', 'aluno4-46', 'Sim', [turma4], ['pai4-46', 'mãe4-46'], 'pai4-46@gmail.com', '4-46', segmentosEnsino[1].segmento)
aluno37 = Aluno('aluno4-47', '4-47', '4-47', '4-47', 'aluno4-47', 'aluno4-47@gmail.com', 'aluno4-47', 'Sim', [turma4], ['pai4-47', 'mãe4-47'], 'pai4-47@gmail.com', '4-47', segmentosEnsino[1].segmento)
aluno38 = Aluno('aluno4-48', '4-48', '4-48', '4-48', 'aluno4-48', 'aluno4-48@gmail.com', 'aluno4-48', 'Sim', [turma4], ['pai4-48', 'mãe4-48'], 'pai4-48@gmail.com', '4-48', segmentosEnsino[1].segmento)
aluno39 = Aluno('aluno4-49', '4-49', '4-49', '4-49', 'aluno4-49', 'aluno4-49@gmail.com', 'aluno4-49', 'Sim', [turma4], ['pai4-49', 'mãe4-49'], 'pai4-49@gmail.com', '4-49', segmentosEnsino[1].segmento)
aluno40 = Aluno('aluno4-50', '4-50', '4-50', '4-50', 'aluno4-50', 'aluno4-50@gmail.com', 'aluno4-50', 'Sim', [turma4], ['pai4-50', 'mãe4-50'], 'pai4-50@gmail.com', '4-50', segmentosEnsino[1].segmento)
alunos4 = [aluno31, aluno32, aluno33, aluno34, aluno35, aluno36, aluno37, aluno38, aluno39, aluno40]
professor4 = Professor('professor1-4', '1-4', '1-4', '1-4', 'professor1-4', 'professor1-4@gmail.com', 'professor1-4', 'Sim', [], '1-4', [], [])


turma5 = Turma('turma5', segmentosEnsino[1].segmento, segmentosEnsino[1].cursos[1], '2024', [], [], [], 'Sim')
aluno41 = Aluno('aluno5-51', '5-51', '5-51', '5-51', 'aluno5-51', 'aluno5-51@gmail.com', 'aluno5-51', 'Sim', [turma5], ['pai5-51', 'mãe5-51'], 'pai5-51@gmail.com', '5-51', segmentosEnsino[1].segmento)
aluno42 = Aluno('aluno5-52', '5-52', '5-52', '5-52', 'aluno5-52', 'aluno5-52@gmail.com', 'aluno5-52', 'Sim', [turma5], ['pai5-52', 'mãe5-52'], 'pai5-52@gmail.com', '5-52', segmentosEnsino[1].segmento)
aluno43 = Aluno('aluno5-53', '5-53', '5-53', '5-53', 'aluno5-53', 'aluno5-53@gmail.com', 'aluno5-53', 'Sim', [turma5], ['pai5-53', 'mãe5-53'], 'pai5-53@gmail.com', '5-53', segmentosEnsino[1].segmento)
aluno44 = Aluno('aluno5-54', '5-54', '5-54', '5-54', 'aluno5-54', 'aluno5-54@gmail.com', 'aluno5-54', 'Sim', [turma5], ['pai5-54', 'mãe5-54'], 'pai5-54@gmail.com', '5-54', segmentosEnsino[1].segmento)
aluno45 = Aluno('aluno5-55', '5-55', '5-55', '5-55', 'aluno5-55', 'aluno5-55@gmail.com', 'aluno5-55', 'Sim', [turma5], ['pai5-55', 'mãe5-55'], 'pai5-55@gmail.com', '5-55', segmentosEnsino[1].segmento)
aluno46 = Aluno('aluno5-56', '5-56', '5-56', '5-56', 'aluno5-56', 'aluno5-56@gmail.com', 'aluno5-56', 'Sim', [turma5], ['pai5-56', 'mãe5-56'], 'pai5-56@gmail.com', '5-56', segmentosEnsino[1].segmento)
aluno47 = Aluno('aluno5-57', '5-57', '5-57', '5-57', 'aluno5-57', 'aluno5-57@gmail.com', 'aluno5-57', 'Sim', [turma5], ['pai5-57', 'mãe5-57'], 'pai5-57@gmail.com', '5-57', segmentosEnsino[1].segmento)
aluno48 = Aluno('aluno5-58', '5-58', '5-58', '5-58', 'aluno5-58', 'aluno5-58@gmail.com', 'aluno5-58', 'Sim', [turma5], ['pai5-58', 'mãe5-58'], 'pai5-58@gmail.com', '5-58', segmentosEnsino[1].segmento)
aluno49 = Aluno('aluno5-59', '5-59', '5-59', '5-59', 'aluno5-59', 'aluno5-59@gmail.com', 'aluno5-59', 'Sim', [turma5], ['pai5-59', 'mãe5-59'], 'pai5-59@gmail.com', '5-59', segmentosEnsino[1].segmento)
aluno50 = Aluno('aluno5-60', '5-60', '5-60', '5-60', 'aluno5-60', 'aluno5-60@gmail.com', 'aluno5-60', 'Sim', [turma5], ['pai5-60', 'mãe5-60'], 'pai5-60@gmail.com', '5-60', segmentosEnsino[1].segmento)
alunos5 = [aluno41, aluno42, aluno43, aluno44, aluno45, aluno46, aluno47, aluno48, aluno49, aluno50]
professor5 = Professor('professor1-5', '1-5', '1-5', '1-5', 'professor1-5', 'professor1-5@gmail.com', 'professor1-5', 'Sim', [], '1-5', [], [])

professores = [professor1, professor2, professor3, professor4, professor5]

disciplina1 = Disciplina('1', '1-1', segmentosEnsino[0].segmento, professores[0], 'Sim')
disciplina2 = Disciplina('2', '1-2', segmentosEnsino[0].segmento, professores[1], 'Sim')
disciplina3 = Disciplina('3', '1-3', segmentosEnsino[0].segmento, professores[2], 'Sim')
disciplina4 = Disciplina('4', '1-4', segmentosEnsino[1].segmento, professores[3], 'Sim')
disciplina5 = Disciplina('5', '1-5', segmentosEnsino[1].segmento, professores[4], 'Sim')

alunos = alunos1 + alunos2 + alunos3 + alunos4 + alunos5
disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]
turmas = [turma1, turma2, turma3, turma4, turma5]

for i in range(len(professores)):
    professores[i].disciplinas.append(disciplinas[i])
    professores[i].turmas.append(turmas[i])
    if i < 3:
        professores[i].segmentos.append(segmentosEnsino[0].segmento)
    else:
        professores[i].segmentos.append(segmentosEnsino[1].segmento)


for i in range(len(turmas)):
    if i == 0:
        for j in range(0,10):
            turmas[i].alunos.append(alunos[j])
    elif i == 1:
        for j in range(10, 20):
            turmas[i].alunos.append(alunos[j])
    elif i == 2:
        for j in range(20, 30):
            turmas[i].alunos.append(alunos[j])
    elif i == 3:
        for j in range(30, 40):
            turmas[i].alunos.append(alunos[j])
    elif i == 4:
        for j in range(40, 50):
            turmas[i].alunos.append(alunos[j])
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

    x = 0
    segmentoEnsino = input('Segmento de Ensino: ')
    for i in range(len(segmentosEnsino)):
        if segmentoEnsino == segmentosEnsino[i].segmento:
            print(f'Segmento de Ensino {segmentoEnsino} existente!')
            x += 1
    if x == 0:
        print(f'Segmento de Ensino {segmentoEnsino} é inexistente!')
        return

    opcaoCurso = input('Opção de Curso: ')
    for i in range(len(segmentosEnsino)):
        for j in range(len(segmentosEnsino[i].cursos)):
            if opcaoCurso == segmentosEnsino[i].cursos[j]:
                print(f'Opção de Curso {opcaoCurso} compatível!')
                x += 1
    if x == 0:
        print(f'Opção de Curso {opcaoCurso} é incompatível ou inexistente!')
        return

    anoEscolar = input('Ano Escolar: ')

    alunosY = []
    while True:
        try:
            alunosX = int(input('Quantidade de Alunos:'))
            for i in range(alunosX):
                x = 0
                nomeX = input('Insira o nome do Estudante: ')
                for j in range(len(alunos)):
                    if nomeX == alunos[j].nome:
                        alunosY.append(alunos[j])
                        print('Aluno existente!')
                        x += 1
                if x == 0:
                    print('Aluno Inexistente!')
                    return
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
                    return
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
                    return
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue
    
    ativo = input('A turma será ativa?')
    if ativo.upper() == 'SIM':
        ativo = 'Sim'
    elif ativo.upper() == 'NÃO':
        ativo = 'Não'
    else:
        print('Opção Inválida!')
        return
    
    turmaX = Turma(nome, segmentoEnsino, opcaoCurso, anoEscolar, alunosY, professoresY, disciplinasY, ativo)
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
        print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SEGMENTO DE ENSINO':
        if turmas[turma].segmentoEnsino.upper() == 'ENSINO MEDIO':
            turmas[turma].segmentoEnsino = segmentosEnsino[1].segmento
            print(f'Segmento de Ensino alterado para: {turmas[turma].segmentoEnsino}')
        elif turmas[turma].segmentoEnsino.upper() == 'ENSINO SUPERIOR':
            turmas[turma].segmentoEnsino = segmentosEnsino[0].segmento
            print(f'Segmento de Ensino alterado para: {turmas[turma].segmentoEnsino}')
        print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
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
        print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'ANO ESCOLAR':
        anoEscolarX = input('Insira um novo Ano Escolar:')
        turmas[turma].anoEscolar = anoEscolarX
        print(f'Ano Escolar alterado para: {anoEscolarX}')
        print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
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
                if alunoX == alunos[i].nome:
                    print(f'Aluno {alunos[i].nome} adicionado!')
                    turmas[turma].alunos.append(alunos[i])
                    x += 1
            if x == 0:
                print(f'O Aluno {alunoX} é inexistente!')
        print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
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
        print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
        return

    elif opcaoX.upper() == 'DISCIPLINAS':
        escolha = input('Você deseja remover ou adicionar uma Disciplina? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            disciplinaX = input('Insira o ID da Disciplina que você deseja remover: ')
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
        print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
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
    print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
    return

#===========================================================================
def excluirTurma(turma):
    opcaoX = input('Você tem certeza de que deseja excluir a turma? ')
    if opcaoX.upper() == 'SIM':
        turmas.remove(turmas[turma])
        print('Turma selecionada excluída!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    print(turmas[turma]) #TEM QUE TIRAR DEPOIS *****
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
    elif opcao.upper() == 'SAIR':
        return
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
    else:
        print('Opção Inválida!')

    return

#DISCIPLINAS ==================================================================================================================================================================

#=========================================================================== inserir
def inserirDisciplina():
    print('Insira as seguintes informações: ')

    x = 0
    id = input('Insira o ID: ')
    for i in range(len(disciplinas)):
        if id == disciplinas[i].id:
            print(f'O ID {id} não está livre!')
            x += 1
            return
    if x == 0:
        print(f'O ID {id} está livre!')

    descricao = input('Insira a descrição: ')
    
    x = 0
    segmento = input('Insira o Segmento de Ensino: ')
    for i in range(len(segmentosEnsino)):
        if segmento == segmentosEnsino[i].segmento:
            print(f'Segmento de Ensino {segmento} existente!')
            x += 1
    if x == 0:
        print(f'Segmento de Ensino {segmento} é inexistente!')
        return
    
    x = 0
    professorTitular = input('Insira o Professor Titular: ')
    for i in range(len(professores)):
        if professorTitular == professores[i].nome:
            print(f'Professor {professores[i].nome} existente!')
            x += 1
    if x == 0:
        print(f'O Professor {professorTitular} é inexistente!')
        return

    ativo = input('A disciplina será ativa? ')
    if ativo.upper() == 'SIM':
        ativo = 'Sim'
    elif ativo.upper() == 'NÃO':
        ativo = 'Não'

    disciplinaX = Disciplina(id, descricao, segmento, professorTitular, ativo)
    disciplinas.append(disciplinaX)
    print(disciplinaX)

    return
#=========================================================================== editar
def editarDisciplina(disciplina):
    print('O que você deseja editar?')
    print('''
ID
Descrição
Segmento De Ensino
Professor Titular
''')
    opcaoX = input('')

    if opcaoX.upper() == 'ID':
        x = 0
        idX = input('Insira o ID: ')
        for i in range(len(disciplinas)):
            if idX == disciplinas[i].id:
                print(f'O ID {idX} não está livre!')
                x += 1
                return
        if x == 0:
            print(f'O ID {idX} está livre, e foi cadastrado!')
            disciplinas[disciplina].id = idX
        print(disciplinas[disciplina]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'DESCRIÇÃO':
        descricaoX = input('Insira a Descrição: ')
        disciplinas[disciplina].descricao = descricaoX
        print(disciplinas[disciplina]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SEGMENTO DE ENSINO':
        if disciplinas[disciplina].segmento.upper() == 'ENSINO MEDIO':
            disciplinas[disciplina].segmento = segmentosEnsino[1].segmento
            print(f'Segmento de Ensino alterado para: {disciplinas[disciplina].segmento}')
        elif disciplinas[disciplina].segmento.upper() == 'ENSINO SUPERIOR':
            disciplinas[disciplina].segmento = segmentosEnsino[0].segmento
            print(f'Segmento de Ensino alterado para: {disciplinas[disciplina].segmento}')
        print(disciplinas[disciplina]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'PROFESSOR TITULAR':
        x = 0
        professorX = input('Insira o Professor que você deseja por no lugar: ')
        for i in range(len(professores)):
            if professorX == professores[i].nome:
                print(f'Professor {professores[i].nome} posto no lugar!')
                disciplinas[disciplina].professorTitular = professores[i]
                x += 1
        if x == 0:
            print(f'O Professor {professorX} é inexistente!')
        print(disciplinas[disciplina]) #TEM QUE TIRAR DEPOIS *****
    return

#=========================================================================== desativar
def desativarDisciplina(disciplina):
    opcaoX = input('Você tem certeza de que deseja desativar a disciplina? ')
    if opcaoX.upper() == 'SIM':
        disciplinas[disciplina].ativo = 'Não'
        print(f'Turma {disciplinas[disciplina].id} desativada!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    print(disciplinas[disciplina]) #TEM QUE TIRAR DEPOIS *****
    return

#=========================================================================== excluir
def excluirDisciplina(disciplina):
    opcaoX = input('Você tem certeza de que deseja excluir a disciplina? ')
    if opcaoX.upper() == 'SIM':
        turmas.remove(disciplinas[disciplina])
        print('Disciplina selecionada excluída!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    print(disciplinas[disciplina]) #TEM QUE TIRAR DEPOIS *****
    return

#===========================================================================
def crudDisciplina():
    print('O que fazer com a disciplina?')
    print('''
Inserir
Editar
Desativar
Excluir
sair
''')
    opcao = input()

    if opcao.upper() == 'INSERIR':
        return inserirDisciplina()
    elif opcao.upper() == 'SAIR':
        return
    else:
        print('qual disciplina acessar?')
        for i in range(len(disciplinas)):
            print(f'{i+1}º Disciplina: {disciplinas[i].descricao}')
        escolha = int(input())-1
    
    if opcao.upper() == 'EDITAR':
        return editarDisciplina(escolha)
    elif opcao.upper() == 'DESATIVAR':
        return desativarDisciplina(escolha)
    elif opcao.upper() == 'EXCLUIR':
        return excluirDisciplina(escolha)
    else:
        print('Opção Inválida!')

    return



#PROFESSORES ==================================================================================================================================================================

#=========================================================================== inserir
def inserirProfessor():
    print('Insira as seguintes informações:')
    nomeX = input('Insira o nome: ')
    sobrenomeX = input('Insira o sobrenome: ')
    enderecoX = input('Insira o endereço: ')
    cpfX = input('Insira o cpf: ')
    nomeUsuarioX = input('Insira o Nome de Usuário: ')
    emailX = input('Insira o email: ')
    senhaX = input('Insira a senha: ')

    ativo = input('O professor será ativo?')
    if ativo.upper() == 'SIM':
        ativo = 'Sim'
    elif ativo.upper() == 'NÃO':
        ativo = 'Não'
    else:
        print('Opção Inválida!')
        return
    
    turmasY = []
    while True:
        try:
            turmasX = int(input('Quantidade de Turmas: '))
            for i in range(turmasX):
                x = 0
                nomeY = input('Insira o nome da Turma: ')
                for j in range(len(turmas)):
                    if nomeY == turmas[j].nome:
                        turmasY.append(turmas[j])
                        print('Turma existente!')
                        x += 1
                if x == 0:
                    print('Turma Inexistente!')
                    return
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue


    formacaoX = input('Insira a formação: ')

    disciplinasY = []
    while True:
        try:
            disciplinasX = int(input('Quantidade de Disciplinas: '))
            for i in range(disciplinasX):
                x = 0
                idX = input('Insira o id da Disciplina: ')
                for j in range(len(disciplinas)):
                    if idX == disciplinas[j].id:
                        disciplinasY.append(disciplinas[j])
                        print('Disciplina existente!')
                        x += 1
                if x == 0:
                    print('Disciplina Inexistente!')
                    return
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue
    
    segmentosY = []
    while True:
        try:
            segmentosX = int(input('Quantidade de Segmentos de Ensino: '))
            for i in range(segmentosX):
                x = 0
                nomeY = input('Insira o Segmento de Ensino: ')
                for j in range(len(segmentosEnsino)):
                    if nomeY == segmentosEnsino[j].segmento:
                        segmentosY.append(segmentosEnsino[j])
                        print('Segmento de Ensino existente!')
                        x += 1
                if x == 0:
                    print('Segmento de Ensino Inexistente!')
                    return
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue
    
    professorX = Professor(nomeX, sobrenomeX, enderecoX, cpfX, nomeUsuarioX, emailX, senhaX, ativo, turmasY, formacaoX, disciplinasY, segmentosY)
    professores.append(professorX)
    print(professorX)

    return
#=========================================================================== editar
def editarProfessor(professor):
    print('O que você deseja editar? ')
    print('''
Nome
Sobrenome
Endereço
CPF
Nome de Usuário
Email
Senha
Turmas
Formação
Disciplinas
Segmentos''')
    opcaoX = input('')

    if opcaoX.upper() == 'NOME':
        nomeX = input('Insira o novo nome: ')
        professores[professor].nome = nomeX
        print(f'Nome alterado para: {professores[professor].nome}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SOBRENOME':
        sobrenomeX = input('Insira o novo sobrenome: ')
        professores[professor].sobrenome = sobrenomeX
        print(f'Sobrenome alterado para: {professores[professor].sobrenome}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'ENDEREÇO':
        enderecoX = input('Insira o novo endereço: ')
        professores[professor].endereco = enderecoX
        print(f'Endereço alterado para: {professores[professor].endereco}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'CPF':
        cpfX = input('Insira o novo CPF: ')
        professores[professor].cpf = cpfX
        print(f'CPF alterado para: {professores[professor].cpf}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'NOME DE USUÁRIO':
        nomeUsuarioX = input('Insira o novo Nome de Usuário: ')
        professores[professor].nomeUsuario = nomeUsuarioX
        print(f'Nome de Usuário alterado para: {professores[professor].nomeUsuario}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'EMAIL':
        emailX = input('Insira o novo Email: ')
        professores[professor].email = emailX
        print(f'Email alterado para: {professores[professor].email}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SENHA':
        senhaX = input('Insira a nova Senha: ')
        professores[professor].senha = senhaX
        print(f'Senha alterada para: {professores[professor].senha}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'TURMAS':
        escolha = input('Você deseja remover ou adicionar uma Turma? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            turmaX = input('Insira a Turma que você deseja remover: ')
            for i in range(len(professores[professor].turmas)):
                if turmaX == professores[professor].turmas[i].nome:
                    print(f'Turma {professores[professor].turmas[i].nome} removida!')
                    professores[professor].turmas.pop(i)
                    x += 1
                    break
            if x == 0:
                print(f'A turma {turmaX} é inexistente!')
        elif escolha.upper() == 'ADICIONAR':
            x = 0
            turmaX = input('Insira a turma que você deseja adicionar: ')
            for i in range(len(turmas)):
                if turmaX == turmas[i].nome:
                    print(f'Turma {turmas[i].nome} adicionada!')
                    professores[professor].turmas.append(turmas[i])
                    x += 1
            if x == 0:
                print(f'A turma {turmaX} é inexistente!')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'FORMAÇÃO':
        formacaoX = input('Insira a nova Formação: ')
        professores[professor].formacao = formacaoX
        print(f'Formação alterada para: {professores[professor].formacao}')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'DISCIPLINAS':
        escolha = input('Você deseja remover ou adicionar uma Disciplina? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            disciplinaX = input('Insira o ID da Disciplina que você deseja remover: ')
            for i in range(len(professores[professor].disciplinas)):
                if disciplinaX == professores[professor].disciplinas[i].id:
                    print(f'Disciplina {professores[professor].disciplinas[i].id} removida!')
                    professores[professor].disciplinas.pop(i)
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
                    professores[professor].disciplinas.append(disciplinas[i])
                    x += 1
            if x == 0:
                print(f'A Disciplina {disciplinaX} é inexistente!')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SEGMENTOS':
        escolha = input('Você deseja remover ou adicionar um Segmento de Ensino? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            segmentoX = input('Insira o Segmento de Ensino que você deseja remover: ')
            for i in range(len(professores[professor].segmentos)):
                if segmentoX == professores[professor].segmentos[i]:
                    print(f'Disciplina {professores[professor].segmentos[i]} removido!')
                    professores[professor].segmentos.pop(i)
                    x += 1
                    break
            if x == 0:
                print(f'O Segmento de Ensino {segmentoX} é inexistente!')
        elif escolha.upper() == 'ADICIONAR':
            x = 0
            segmentoX = input('Insira o Segmento de Ensino que você deseja adicionar: ')
            for i in range(len(segmentosEnsino)):
                if segmentoX == segmentosEnsino[i].segmento:
                    print(f'Segmento de Ensino {segmentosEnsino[i].segmento} adicionado!')
                    professores[professor].segmentos.append(segmentosEnsino[i])
                    x += 1
            if x == 0:
                print(f'O Segmento de Ensino {segmentoX} é inexistente!')
        print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
        return
    
    else:
        print('Opção Inválida!')

    return

#=========================================================================== desativar
def desativarProfessor(professor):
    opcaoX = input('Você tem certeza de que deseja desativar este Professor? ')
    if opcaoX.upper() == 'SIM':
        professores[professor].ativo = 'Não'
        print(f'Turma {professores[professor].nome} desativado!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
    return

#=========================================================================== excluir
def excluirProfessor(professor):
    opcaoX = input('Você tem certeza de que deseja excluir este Professor? ')
    if opcaoX.upper() == 'SIM':
        turmas.remove(professores[professor])
        print('Professor selecionado excluído!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    print(professores[professor]) #TEM QUE TIRAR DEPOIS *****
    return

#===========================================================================
def crudProfessor():
    print('O que fazer com o professor?')
    print('''
Inserir
Editar
Desativar
Excluir
sair
''')
    opcao = input()

    if opcao.upper() == 'INSERIR':
        return inserirProfessor()
    elif opcao.upper() == 'SAIR':
        return
    else:
        print('qual professor acessar?')
        for i in range(len(professores)):
            print(f'{i+1}º Professor: {professores[i].nome}')
        escolha = int(input())-1
    
    if opcao.upper() == 'EDITAR':
        return editarProfessor(escolha)
    elif opcao.upper() == 'DESATIVAR':
        return desativarProfessor(escolha)
    elif opcao.upper() == 'EXCLUIR':
        return excluirProfessor(escolha)
    else:
        print('Opção Inválida!')

    return

#ESTUDANTES ==================================================================================================================================================================

#=========================================================================== inserir
def inserirEstudante():
    print('Insira as seguintes informações: ')
    nomeX = input('Insira o nome: ')
    sobrenomeX = input('Insira o sobrenome: ')
    enderecoX = input('Insira o endereço: ')
    cpfX = input('Insira o cpf: ')
    nomeUsuarioX = input('Insira o Nome de Usuário: ')
    emailX = input('Insira o email: ')
    senhaX = input('Insira a senha: ')

    ativo = input('O estudante será ativo? ')
    if ativo.upper() == 'SIM':
        ativo = 'Sim'
    elif ativo.upper() == 'NÃO':
        ativo = 'Não'
    else:
        print('Opção Inválida!')
        return
    
    segmentoEnsinoX = input('Insira o Segmento de Ensino: ')
    turmaX = ''
    if segmentoEnsinoX == segmentosEnsino[1].segmento:
        print('O estudante cursará dois cursos paralelamente? ')
        escolha = input('')
        if escolha.upper() == 'SIM':
            turmaX = []
            print('Escolha as turmas com seus cursos: ')
            for i in range(len(turmas)):
                if turmas[i].segmentoEnsino == segmentosEnsino[1].segmento:
                    print(f'Turma: {turmas[i].nome} \n Curso: {turmas[i].opcaoCurso}')

            escolhaUm = input('Primeira Turma: ')
            x = 0
            for i in range(len(turmas)):
                if escolhaUm == turmas[i].nome:
                    x += 1
                    turmaX.append(escolhaUm)
            if x == 0:
                print('Turma não existente!')
                return

            escolhaDois = input('Segunda Turma: ')
            x = 0
            for i in range(len(turmas)):
                if escolhaUm == turmas[i].nome:
                    x += 1
                    turmaX.append(escolhaDois)
            if x == 0:
                print('Turma não existente!')
                return

        if escolha.upper() == 'NÃO':
            turmaX = input('Insira a turma: ')
            for i in range(len(turmas)):
                if turmaX == turmas[i].nome:
                    print(f'Turma {turmas[i].nome} existente!')
                    x += 1
            if x == 0:
                print(f'Turma {turmaX} é inexistente!')
                return
    else:
        turmaX = input('Insira a turma: ')
        for i in range(len(turmas)):
            if turmaX == turmas[i].nome:
                print(f'Turma {turmas[i].nome} existente!')
                x += 1
        if x == 0:
            print(f'Turma {turmaX} é inexistente!')
            return

    filiacaoY = []
    while True:
        try:
            filiacaoX = int(input('Insira a quantidade de responsáveis: '))
            for i in range(filiacaoX):
                nomeX = input(f'Insira o nome do {i}º Responsável: ')
                filiacaoY.append(nomeX)
            break
        except:
            print('Não foi inserido um número, tente novamente!')
            continue

    emailResponsavelX = input('Insira o email de um dos responsáveis: ')
    registroAcadX = input('Insira o Registro Acadêmico: ')

    alunoX = Aluno(nomeX, sobrenomeX, enderecoX, cpfX, nomeUsuarioX, emailX, senhaX, ativo, turmaX, filiacaoY, emailResponsavelX, registroAcadX, segmentoEnsinoX)
    alunos.append(alunoX)
    print(alunoX)

    return

#=========================================================================== editar
def editarEstudante(aluno):
    print('O que você deseja editar?')
    print('''
Nome
Sobrenome
Endereço
CPF
Nome de Usuário
Email
Senha
Turma
Filiação
Email Responsável
Registro Acadêmico
Segmento de Ensino
''')
    opcaoX = input('')

    if opcaoX.upper() == 'NOME':
        nomeX = input('Insira o novo nome: ')
        alunos[aluno].nome = nomeX
        print(f'Nome alterado para: {alunos[aluno].nome}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SOBRENOME':
        sobrenomeX = input('Insira o novo sobrenome: ')
        alunos[aluno].sobrenome = sobrenomeX
        print(f'Sobrenome alterado para: {alunos[aluno].sobrenome}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'ENDEREÇO':
        enderecoX = input('Insira o novo endereço: ')
        alunos[aluno].endereco = enderecoX
        print(f'Endereço alterado para: {alunos[aluno].endereco}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'CPF':
        cpfX = input('Insira o novo CPF: ')
        alunos[aluno].cpf = cpfX
        print(f'CPF alterado para: {alunos[aluno].cpf}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'NOME DE USUÁRIO':
        nomeUsuarioX = input('Insira o novo Nome de Usuário: ')
        alunos[aluno].nomeUsuario = nomeUsuarioX
        print(f'Nome de Usuário alterado para: {alunos[aluno].nomeUsuario}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'EMAIL':
        emailX = input('Insira o novo Email: ')
        alunos[aluno].email = emailX
        print(f'Email alterado para: {alunos[aluno].email}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SENHA':
        senhaX = input('Insira a nova Senha: ')
        alunos[aluno].senha = senhaX
        print(f'Senha alterada para: {alunos[aluno].senha}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'TURMA':
        escolha = input('Você deseja remover ou adicionar uma Turma? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            turmaX = input('Insira a Turma que você deseja remover: ')
            for i in range(len(alunos[aluno].turma)):
                if turmaX == alunos[aluno].turma[i].nome:
                    print(f'Turma {alunos[aluno].turma[i].nome} removida!')
                    alunos[aluno].turma.pop(i)
                    x += 1
                    break
            if x == 0:
                print(f'A turma {turmaX} é inexistente!')
        elif escolha.upper() == 'ADICIONAR':
            x = 0
            turmaX = input('Insira a turma que você deseja adicionar: ')
            for i in range(len(turmas)):
                if turmaX == turmas[i].nome:
                    print(f'Turma {turmas[i].nome} adicionada!')
                    alunos[aluno].turma.append(turmas[i])
                    x += 1
            if x == 0:
                print(f'A turma {turmaX} é inexistente!')
        else:
            print('Opção Inválida!')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return

    elif opcaoX.upper() == 'FILIAÇÃO':
        escolha = input('Você deseja remover ou adicionar uma Filiação? ')
        if escolha.upper() == 'REMOVER':
            x = 0
            filiacaoX = input('Insira a Filiação que você deseja remover: ')
            for i in range(len(alunos[aluno].filiacao)):
                if filiacaoX == alunos[aluno].filiacao[i]:
                    print(f'Filiação {alunos[aluno].filiacao[i]} removida!')
                    alunos[aluno].filiacao.pop(i)
                    x += 1
                    break
            if x == 0:
                print(f'A filiação {filiacaoX} é inexistente!')
        elif escolha.upper() == 'ADICIONAR':
            filiacaoX = input('Insira a Filiação que você deseja adicionar: ')
            alunos[aluno].filiacao.append(filiacaoX)
            print(f'Filiação {filiacaoX} adicionada!')
        else:
            print('Opção Inválida!')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
        
    elif opcaoX.upper() == 'EMAIL RESPONSÁVEL':
        emailResponsavelX = input('Insira o novo Email Responsável: ')
        alunos[aluno].emailResponsavel = emailResponsavelX
        print(f'Email Responsável alterado para: {alunos[aluno].emailResponsavel}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'REGISTRO ACADÊMICO':
        registroAcadX = input('Insira o novo Registro Acadêmico')
        alunos[aluno].registroAcad = registroAcadX
        print(f'Registro Acadêmico alterado para: {alunos[aluno].registroAcad}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return
    
    elif opcaoX.upper() == 'SEGMENTO DE ENSINO':
        if alunos[aluno].segmentoEnsino.upper() == 'ENSINO MEDIO':
            alunos[aluno].segmentoEnsino = segmentosEnsino[1].segmento
            print(f'Segmento de Ensino alterado para: {alunos[aluno].segmentoEnsino}')
        elif alunos[aluno].segmentoEnsino.upper() == 'ENSINO SUPERIOR':
            alunos[aluno].segmentoEnsino = segmentosEnsino[0].segmento
            print(f'Segmento de Ensino alterado para: {alunos[aluno].segmentoEnsino}')
        print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
        return

    else:
        print('Opção Inválida!')

    return

#=========================================================================== desativar
def desativarEstudante(aluno):
    opcaoX = input('Você tem certeza de que deseja desativar este Estudante? ')
    if opcaoX.upper() == 'SIM':
        alunos[aluno].ativo = 'Não'
        print(f'Turma {alunos[aluno].nome} desativado!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
    return

#=========================================================================== excluir
def excluirEstudante(aluno):
    opcaoX = input('Você tem certeza de que deseja excluir este Estudante? ')
    if opcaoX.upper() == 'SIM':
        turmas.remove(alunos[aluno])
        print('Aluno selecionado excluído!')
    elif opcaoX.upper() == 'NÃO':
        return
    else:
        print('Opção Inválida!')
    print(alunos[aluno]) #TEM QUE TIRAR DEPOIS *****
    return

#=========================================================================== transferência
def transferenciaEstudante(aluno):
    if alunos[aluno].segmentoEnsino == segmentosEnsino[0].segmento:
        print('Você deseja transferir o estudante para qual curso?')
        for i in range(len(segmentosEnsino[0].cursos)):
            print(f'{i+1}º curso: {segmentosEnsino[0].cursos[i]}')
        opcaoX = int(input(''))-1

        if alunos[aluno].turma[0].opcaoCurso != segmentosEnsino[0].cursos[opcaoX]:
            print('Estas são as turmas do curso selecionado: ')
            for i in range(len(turmas)):
                if turmas[i].opcaoCurso == segmentosEnsino[1].cursos[opcaoX]:
                    print(f'{i+1}ª turma: {turmas[i].nome}')
            print('Selecione uma das turmas para a transferência!')
            escolha = int(input(''))-1
            alunos[aluno].turma[0] = turmas[escolha]
            print(f'Estudante transferido para a turma {alunos[aluno].turma[0].opcaoCurso}')
        else:
            print('O curso selecionado é o atual do estudante!')

    elif alunos[aluno].segmentoEnsino == segmentosEnsino[1].segmento:
        if len(alunos[aluno].turma) > 1:
            print('O estudante é do Ensino Superior e já está matriculado nos dois cursos!')
        else:
            print('Você deseja transferir o estudante para qual curso?')
            for i in range(len(segmentosEnsino[1].cursos)):
                print(f'{i+1}º curso: {segmentosEnsino[1].cursos[i]}')
            opcaoX = int(input(''))-1

            if alunos[aluno].turma[0].opcaoCurso != segmentosEnsino[1].cursos[opcaoX]:
                print('Estas são as turmas do curso selecionado: ')
                for i in range(len(turmas)):
                    if turmas[i].opcaoCurso == segmentosEnsino[1].cursos[opcaoX]:
                        print(f'{i+1}ª turma: {turmas[i].nome}')
                print('Selecione uma das turmas para a transferência!')
                escolha = int(input(''))-1
                alunos[aluno].turma[0] = turmas[escolha]
                print(f'Estudante transferido para a turma {alunos[aluno].turma[0].opcaoCurso}')
            else:
                print('O curso selecionado é o atual do estudante!')
    print(alunos[aluno])
    return

#===========================================================================
def crudEstudante():
    print('O que fazer com o estudante?')
    print('''
Inserir
Editar
Desativar
Excluir
Solicitar Transferência
sair
''')
    opcao = input()

    if opcao.upper() == 'INSERIR':
        return inserirEstudante()
    elif opcao.upper() == 'SAIR':
        return
    else:
        print('qual estudante acessar?')
        for i in range(len(alunos)):
            print(f'{i+1}º Estudante: {alunos[i].nome}')
        escolha = int(input())-1
    
    if opcao.upper() == 'EDITAR':
        return editarEstudante(escolha)
    elif opcao.upper() == 'DESATIVAR':
        return desativarEstudante(escolha)
    elif opcao.upper() == 'EXCLUIR':
        return excluirEstudante(escolha)
    elif opcao.upper() == 'SOLICITAR TRANSFERÊNCIA':
        return transferenciaEstudante(escolha)
    else:
        print('Opção Inválida!')

    return

#PARTE PRÁTICA ==================================================================================================================================================================

"""
1. mecatrônica, eletromecânica e informática. Obrigatoriamente, um aluno do EM deve estar associado a uma dessas opções; fechou ================
2. O aluno do EM pode solicitar transferência para outra opção de curso durante a sua vida acadêmica na instituição; fechou mas posso fazer um tiquito diferente ================

4. O aluno do ensino superior poderá cursar os dois segmentos paralelamente; tenho q arrumar// fechou ================
5. Caso o aluno tenha optado por apenas curso (ciências da computação ou pedagogia), é permitido ao aluno transferir de curso durante a sua vida acadêmica na instituição; fechou mas posso fazer um tiquito diferente ================

6. É possível imprimir, inserir, editar, desativar e excluir uma turma. fechou ================
11. É possível inserir, editar, desativar e excluir uma disciplina; fechou ================
13. É possível inserir, editar, desativar e excluir um professor; fechou ================
15. É possível inserir, editar, desativar e excluir um estudante. fechou ================
filiação é o nome do pai e da mãe fechou ================
"""

print('Bem vindo ao sistema estudantil!')
x = 0
while x == 0:
    print('')
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
        crudDisciplina()
        continue
    elif opcao.upper() == 'PROFESSORES':
        crudProfessor()
        continue
    elif opcao.upper() == 'ESTUDANTES':
        crudEstudante()
        continue
    elif opcao.upper() == 'SAIR':
        break
    else:
        print('Foi inseirdo uma opção inválida: ')
        continue

#modificar o lance do professor, pq é uma lista de disciplinas, segmentos e turmas
#ta individual, logo devo atualizar acho q só oq to fazendo agora, pq o resto nn mexe nessas partes do professor
#arrumei
#falta terminar o editar professor e os tudo sobre os estudantes
#dai também os requisitos específicos
#vapo