#ARQUIVO DESTINADO À FUNÇÕES

#CLASSES
from classes import Aluno
from classes import Professor
from classes import EnsinoMedio
from classes import Superior
from classes import Turma
from classes import Disciplinas

"""
1. mecatrônica, eletromecânica e informática. Obrigatoriamente, um aluno do EM deve estar associado a uma dessas opções; fechou ================
2. O aluno do EM pode solicitar transferência para outra opção de curso durante a sua vida acadêmica na instituição;
4. O aluno do ensino superior poderá cursar os dois segmentos paralelamente;
5. Caso o aluno tenha optado por apenas curso (ciências da computação ou pedagogia), é permitido ao aluno transferir de curso durante a sua vida acadêmica na instituição;
6. É possível imprimir, inserir, editar, desativar e excluir uma turma.
11. É possível inserir, editar, desativar e excluir uma disciplina;
13. É possível inserir, editar, desativar e excluir um professor;
15. É possível inserir, editar, desativar e excluir um estudante.
"""

#CRUD TURMA ==================================================================================================================================================
def crudTurma(turmas, alunos, professores, disciplinas):

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
            escolha = input(f'Digite um número entre 1 e {len(turmas)} para escolher a turma: ')
            print(turmas[escolha-1])

            continue

        #==========================================================
        elif entrada.upper() == "INSERIR":
            print(f'''
Para inserir uma turma, responda tais perguntas:
''')
            nomeX = input('Insira o nome da Turma: ')
            segmentoEnsinoX = input('Insira o Segmento de Ensino: ')
            opcaoCursoX = input('Insira a Opção de Curso: ')
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
            continue
        
        #==========================================================
        elif entrada.upper() == "EDITAR":
            print(f'''
Qual turma você deseja editar?
No momento possuímos {len(turmas)}, sendo:''')
            for i in range(len(turmas)):
                print(f'{i+1}ª turma: {turmas[i].opcaoCurso}')
            escolha = input(f'Digite um número entre 1 e {len(turmas)} para escolher a turma: ')

            print(f'''
    O que você deseja editar?
    Para editar o NOME, insira "nome";
    Para editar o SEGMENTO DE ENSINO, insira "segmento de ensino";
    Para editar a OPÇÃO DE CURSO, insira a "opção de curso";
    Para editar o ANO ESCOLAR, insira "ano escolar";
    Para editar os ALUNOS, insira "alunos";
    Para editar os PROFESSORES, inrira "professores";
    Para editar as DISCIPLINAS, insira "disciplinas".
                  ''')
            editar = input('')
            if editar.upper() == 'NOME':
                

            continue
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