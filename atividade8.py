#ARQUIVO DESTINADO À PRÁTICA 

#CLASSES ==================================================================================================================================================
from classes import Aluno
from classes import Professor
from classes import SegmentoEnsino
#from classes import EnsinoMedio
#from classes import Superior
from classes import Turma
from classes import Disciplinas

#VARIÁVEIS INICIAIS ==================================================================================================================================================

alunosPr = []
professoresPr = []
segmentosEnsinoPr = []
#ensinoMedio = EnsinoMedio(['Mecatrônica', 'Eletromecânica', 'Informática'])
#ensinoSuperior = Superior(['Ciências Da Computação', 'Pedagogia'])
turmasPr = []
disciplinasPr = []

#FUNÇÕES ==================================================================================================================================================

#CRUD TURMA ==================================================================================================================================================
def crudTurma(turmasY, alunosY, professoresY, disciplinasY, segmentosEnsinoY):
    global turmasPr
    turmas = turmasY
    alunos = alunosY
    professores = professoresY
    disciplinas = disciplinasY
    segmentosEnsino = segmentosEnsinoY

    x = 0
    while x == 0:
        print('O que você deseja realizar com a turma?')
        print('''
    Para IMPRIMIR, digite "imprimir";
    Para INSERIR algum estudante, digite "inserir";
    Para EDITAR alguma turma, digite "editar";
    Para DESATIVAR alguma turma, digite "desativar";
    Para EXCLUIR alguma turma, digite "excluir";
    Para SAIR, digite "sair".
              ''')
        entrada = input('')

        #==========================================================
        if entrada.upper() == "IMPRIMIR":
            print(f'''
Qual turma você deseja imprimir?
No momento possuímos {len(turmas)}, sendo:''')
            for i in range(len(turmas)):
                print(f'{i+1}ª turma: {turmas[i].opcaoCurso}')
            escolha = int(input(f'Digite um número entre 1 e {len(turmas)} para escolher a turma: '))
            print(turmas[escolha-1])

            continue

        #==========================================================
        elif entrada.upper() == "INSERIR":
            print(f'''
Para inserir uma turma, responda tais perguntas:
''')
            nomeX = input('Insira o nome da Turma: ')
            
            verificar = 0
            while verificar == 0:
                segmentoEnsinoX = input('Insira o Segmento de Ensino: ')
                for i in range(len(segmentosEnsino)):
                    if segmentoEnsinoX == segmentosEnsino[i].segmento:
                        verificar += 1
                        print('Segmento de Ensino Válida!')
                if verificar == 0:
                    print('Segmento de Ensino Inválido!')

            verificar = 0
            while verificar == 0:
                opcaoCursoX = input('Insira a Opção de Curso: ')
                for i in range(len(segmentosEnsino)):
                    for j in range(len(segmentosEnsino[i].cursos)):
                        if segmentosEnsino[i].cursos[j] == opcaoCursoX:
                            verificar += 1
                            print('Opção de Curso Válida!')
                if verificar == 0:
                    print('Opção de Curso Inválida!')

            anoEscolarX = input('Insira o Ano Escolar:')
            
            alunosX = []
            qntdAlunos = int(input('Quantos alunos a turma terá?'))
            for i in range(qntdAlunos):
                alunoX = input('Insira o nome do Aluno:')
                for j in range(len(alunos)):
                    if alunos[j] == alunoX:
                        alunosX.append(alunos[j])
                        print(f'Aluno {alunoX} adicionado à Turma!')

            professoresX = []
            qntdProfessores = int(input('Quantos professores a turma terá?'))
            for i in range(qntdProfessores):
                professorX = input('Insira o nome do Professor:')
                for j in range(len(professores)):
                    if professores[j] == professorX:
                        professoresX.append(professores[i])
                        print(f'Professor {professorX} adicionado à Turma!')
            
            disciplinasX = []
            qntdDisciplinas = int(input('Quantas disciplinas a turma terá?'))
            for i in range(qntdDisciplinas):
                disciplinaX = input('Insira o nome da Disciplina')
                for j in range(len(disciplinas)):
                    if disciplinas[i] == disciplinaX:
                        disciplinasX.append(disciplinas[i])
                        print(f'Disciplina {disciplinasX} adicionada à Turma!')

            turmaX = Turma(nomeX, segmentoEnsinoX, opcaoCursoX, anoEscolarX, alunosX, professoresX, disciplinasX)
            turmas.append(turmaX)
            print('Turma Criada!')
        
        #==========================================================
        elif entrada.upper() == "EDITAR":
            print(f'''
Qual turma você deseja editar?
No momento possuímos {len(turmas)}, sendo:''')
            for i in range(len(turmas)):
                print(f'{i+1}ª turma: {turmas[i].opcaoCurso}')
            escolha = int(input(f'Digite um número entre 1 e {len(turmas)} para escolher a turma: '))

            print(f'''
    O que você deseja editar?
    Para editar o NOME, insira "nome";
    Para editar o SEGMENTO DE ENSINO, insira "segmento de ensino";
    Para editar a OPÇÃO DE CURSO, insira a "opção de curso";
    Para editar o ANO ESCOLAR, insira "ano escolar";
    Para editar os ALUNOS, insira "alunos";
    Para editar os PROFESSORES, inrira "professores";
    Para editar as DISCIPLINAS, insira "disciplinas";
    Para cancelar, insira "sair".
                  ''')
            editar = input('')

            if editar.upper() == 'NOME':
                edicao = input('Insira o novo nome: ')
                turmas[escolha].nome = edicao
                print(f'Nome modificado para {edicao}!')
                print(turmas[escolha].nome)
                turmasPr = turmas
                return turmas


            elif editar.upper() == 'SEGMENTO DE ENSINO':
                if (turmas[escolha].segmentoEnsino).upper() == 'ENSINO MEDIO':
                    turmas[escolha].segmentoEnsino = 'Ensino Superior'
                    print('Segmento de Ensino modificado para Ensino Superior!')
                    return turmas
                elif (turmas[escolha.segmentoEnsino]).upper() == 'ENSINO SUPERIOR':
                    turmas[escolha].segmentoEnsino = 'Ensino Medio'
                    print('Segmento de Ensino modificado para Ensino Médio!')
                    turmasPr = turmas
                    return turmas


            elif editar.upper() == 'OPÇÃO DE CURSO':
                verificar = 0
                while verificar == 0:
                    edicao = input('Insira a nova Opção de Curso: ')
                    for i in range(len(segmentosEnsino)):
                        for j in range(len(segmentosEnsino[i].cursos)):
                            if segmentosEnsino[i].cursos[j] == edicao:
                                verificar += 1
                        if verificar == 0:
                            print('Opção de Curso Válida!')
                            turmas[escolha].opcaoCurso = edicao
                            turmasPr = turmas
                            return turmas
                        else:
                            print(f'Opção de Curso Inválida!')


            elif editar.upper() == 'ANO ESCOLAR':
                edicao = input('Insira o novo Ano Escolar:')
                turmas[escolha].anoEscolar = edicao
                print(f'Ano Escolar modificado para {edicao}!')
                turmasPr = turmas
                return turmas


            elif editar.upper() == 'ALUNOS':
                print(len(turmas[escolha].alunos))
                edicaoAluno = input('Você deseja remover ou adicionar algum aluno? ')
                if edicaoAluno.upper() == 'REMOVER':
                    verificar = 0
                    while verificar == 0:
                        edicao = input('Qual aluno você deseja remover? ')
                        for i in range(len(turmas[escolha].alunos)):
                            if edicao == turmas[escolha].alunos[i].nome:
                                verificar += 1
                                turmas[escolha].alunos.pop(i)
                                print('Aluno removido!')
                                turmasPr = turmas
                                return turmas
                        if verificar == 0:
                                print('O aluno informado não existe na turma!')
                elif edicaoAluno.upper() == 'ADICIONAR':
                    edicao = input('Insira o nome do estudante que você deseja adicionar: ')
                    verificar = -1
                    for i in range(len(alunos)):
                        if edicao == alunos[i].nome:
                            turmas[escolha].alunos.append(alunos[i])
                            verificar = i
                    if verificar > -1:
                        turmas[escolha].alunos.append(alunos[verificar])
                        print('Aluno adicionado!')
                        turmasPr = turmas
                        return turmas



            elif editar.upper() == 'PROFESSORES':
                edicaoProfessor = input('Você deseja remover ou adicionar algum professor?')
                if edicaoProfessor.upper() == 'REMOVER':
                    verificar = 0
                    while verificar == 0:
                        edicao = input('Qual professor você deseja remover? ')
                        for i in range(len(turmas[escolha].professores)):
                            if edicao == turmas[escolha].professores[i].nome:
                                verificar += 1
                                turmas[escolha].professores.pop(i)
                                print('Professor removido!')
                                turmasPr = turmas
                                return turmas
                        if verificar == 0:
                                print('O professor informado não existe na turma!')
                elif edicaoProfessor.upper() == 'ADICIONAR':
                    edicao = input('Insira o nome do professor que você deseja adicionar: ')
                    verificar = -1
                    for i in range(len(professores)):
                        if edicao == professores[i].nome:
                            verificar = i
                    if verificar > -1:
                        (turmas[escolha].professores).append(professores[verificar])
                        print('Professor adicionado!')
                        turmasPr = turmas
                        return turmas


            elif editar.upper() == 'SAIR':
                print('')
                turmasPr = turmas
                return turmas
        #==========================================================
        elif entrada.upper() == "DESATIVAR":
            print('')
            continue
        elif entrada.upper() == "EXCLUIR":
            print('')
            continue
        elif entrada.upper() == "SAIR":
            print('')
            break
        else:
            print('Foi escrito algum comando desconhecido!')

        return ''

#CRUD DISCIPLINA ==================================================================================================================================================
def crudDisciplina():
    return ''

#CRUD PROFESSOR ==================================================================================================================================================
def crudProfessor():
    return ''

#CRUD ALUNO ==================================================================================================================================================
def crudAluno():
    return ''

#SEGMENTO DE ENSINO ==================================================================================================================================================
segmentoEnsinoX = SegmentoEnsino('Ensino Médio', ['Mecatrônica', 'Eletromecânica', 'Informática'])
segmentosEnsinoPr.append(segmentoEnsinoX)
segmentoEnsinoX = SegmentoEnsino('Ensino superior', ['Ciências Da Computação', 'Pedagogia'])
segmentosEnsinoPr.append(segmentoEnsinoX)

#PROFESSOR ==================================================================================================================================================
#conectar disciplinas
for i in range(5):
    if i < 3:
        professorX = Professor(('professor' + str(i)), str(i), ('endereço' + str(i)), ('cpf', str(i)), [], ('professor.' + str(i)), ('prf' + str(i) + '@gmail.com'), ('prf' + str(i)), ('Formado em' + str(i)), [], segmentosEnsinoPr[0].segmento)
        professoresPr.append(professorX)
        print(professorX)
    else:
        professorX = Professor(('professor' + str(i)), str(i), ('endereço' + str(i)), ('cpf', str(i)), [], ('professor.' + str(i)), ('prf' + str(i) + '@gmail.com'), ('prf' + str(i)), ('Formado em' + str(i)), [], segmentosEnsinoPr[1].segmento)
        professoresPr.append(professorX)
        print(professorX)


#DISCIPLINAS fechou ==================================================================================================================================================
for i in range(5):
    if i < 3:
        disciplinaX = Disciplinas(i, f'Disciplina número {i}', segmentosEnsinoPr[0].segmento, professoresPr[i])
        disciplinasPr.append(disciplinaX)
        print(disciplinaX)
    else:
        disciplinaX = Disciplinas(i, f'Disciplina número {i}', segmentosEnsinoPr[1].segmento, professoresPr[i])
        disciplinasPr.append(disciplinaX)
        print(disciplinaX)


#TURMAS ==================================================================================================================================================
#arrumar o lance de atrelar os estudantes
for i in range(5):
    if i < 3:
        turmaX = Turma(('turma' + str(i)), 'Ensino Médio', segmentosEnsinoPr[0].cursos[i], '2024', [], [professoresPr[i]], [disciplinasPr[i]])
        turmasPr.append(turmaX)
        print(turmaX)
    else:
        turmaX = Turma(('turma' + str(i)), 'Ensino Superior', segmentosEnsinoPr[1].cursos[i-3], '2024', [], [professoresPr[i]], [disciplinasPr[i]])
        turmasPr.append(turmaX)
        print(turmaX)


#ALUNOS ==================================================================================================================================================
for i in range(5):
    alunosTemporario = []
    for j in range(20):
        if i < 3:
            alunoX = Aluno(('aluno' + str(i) + '-' + str(j)), (str(i) + '-' + str(j)), ('endereco' + str(i) + '-' + str(j)), ('cpf' + str(i) + '-' + str(j)), ('aln' + str(i) + '-' + str(j)), ('aln.' + str(i) + '-' + str(j) + '@gmail.com'), ('aln.' + str(i) + '-' + str(j)), turmasPr[i], (str(i) + '-' + str(j)), ('pai.' + str(i) + '-' + str(j)), (str(i) + '-' + str(j)), segmentosEnsinoPr[0].segmento)
            alunosPr.append(alunoX)
            alunosTemporario.append(alunoX)
            print(alunoX)
        else:
            alunoX = Aluno(('aluno' + str(i) + '-' + str(j)), (str(i) + '-' + str(j)), ('endereco' + str(i) + '-' + str(j)), ('cpf' + str(i) + '-' + str(j)), ('aln' + str(i) + '-' + str(j)), ('aln.' + str(i) + '-' + str(j)), ('aln.' + str(i) + '-' + str(j) + '@gmail.com'), turmasPr[i], (str(i) + '-' + str(j)), '', (str(i) + '-' + str(j)), segmentosEnsinoPr[1].segmento)
            alunosPr.append(alunoX)
            alunosTemporario.append(alunoX)
            #print(alunoX)

    turmasPr[i].alunos = alunosTemporario

for i in range(5):
    
    print('')

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

print('')
print(turmasPr[3].alunos[2])
print('')

#PRÁTICA ==================================================================================================================================================

entrada = ''

print('Seja bem vindo ao sistema estudantil!')

#tem q arrumar essa bomba aqui, o Fim nn ta funcionando, só o fim
while (entrada.upper() != "FIM"):
    print('O que você deseja fazer agora?')
    print(f'''
Para editar alguma TURMA, digite "turma";
Para editar alguma DISCIPLINA, digite "disciplina";
Para editar algum(a) PROFESSOR, digite "professor";
Para editar algum(a) ALUNO, digite "aluno";
Para FINALIZAR o atendimento, digite "fim".''')
    entrada = input('')

    if entrada.upper() == 'TURMA':
        turmasPr = crudTurma(turmasPr, alunosPr, professoresPr, disciplinasPr, segmentosEnsinoPr)
    elif entrada.upper() == 'DISCIPLINA':
        crudDisciplina()
    elif entrada.upper() == 'PROFESSOR':
        crudProfessor()
    elif entrada.upper() == 'ALUNO':
        crudAluno()
    elif entrada.upper() != 'FIM':
        print('Foi escrito algum comando desconhecido!')

#entendi o problema, as alterações são no arquivo das funções, e permanecem lá
#acho q faz sentido passar a geração dos dados pra lá, e manter os dados registrados lá, e aqui somente a "cara"
#vai ficar desorganizado, mas é a vida
#eeee, vou ter q editar bastante coisa, EU ACHO, mas se resolver o problema