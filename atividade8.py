#ARQUIVO DESTINADO À PRÁTICA 

#CLASSES ==================================================================================================================================================
from classes import Aluno
from classes import Professor
from classes import SegmentoEnsino
#from classes import EnsinoMedio
#from classes import Superior
from classes import Turma
from classes import Disciplinas

#FUNÇÕES ==================================================================================================================================================
from funcoes import crudAluno
from funcoes import crudProfessor
from funcoes import crudTurma
from funcoes import crudDisciplina

#VARIÁVEIS INICIAIS ==================================================================================================================================================
alunos = []
professores = []
segmentosEnsino = []
#ensinoMedio = EnsinoMedio(['Mecatrônica', 'Eletromecânica', 'Informática'])
#ensinoSuperior = Superior(['Ciências Da Computação', 'Pedagogia'])
turmas = []
disciplinas = []

#SEGMENTO DE ENSINO ==================================================================================================================================================
segmentoEnsinoX = SegmentoEnsino('Ensino Médio', ['Mecatrônica', 'Eletromecânica', 'Informática'])
segmentosEnsino.append(segmentoEnsinoX)
segmentoEnsinoX = SegmentoEnsino('Ensino superior', ['Ciências Da Computação', 'Pedagogia'])
segmentosEnsino.append(segmentoEnsinoX)

#PROFESSOR ==================================================================================================================================================
#conectar disciplinas
for i in range(5):
    if i < 3:
        professorX = Professor(('professor' + str(i)), str(i), ('endereço' + str(i)), ('cpf', str(i)), [], ('professor.' + str(i)), ('prf' + str(i) + '@gmail.com'), ('prf' + str(i)), ('Formado em' + str(i)), [], segmentosEnsino[0].segmento)
        professores.append(professorX)
        print(professorX)
    else:
        professorX = Professor(('professor' + str(i)), str(i), ('endereço' + str(i)), ('cpf', str(i)), [], ('professor.' + str(i)), ('prf' + str(i) + '@gmail.com'), ('prf' + str(i)), ('Formado em' + str(i)), [], segmentosEnsino[1].segmento)
        professores.append(professorX)
        print(professorX)


#DISCIPLINAS fechou ==================================================================================================================================================
for i in range(5):
    if i < 3:
        disciplinaX = Disciplinas(i, f'Disciplina número {i}', segmentosEnsino[0].segmento, professores[i])
        disciplinas.append(disciplinaX)
        print(disciplinaX)
    else:
        disciplinaX = Disciplinas(i, f'Disciplina número {i}', segmentosEnsino[1].segmento, professores[i])
        disciplinas.append(disciplinaX)
        print(disciplinaX)


#TURMAS ==================================================================================================================================================
#arrumar o lance de atrelar os estudantes
for i in range(5):
    if i < 3:
        turmaX = Turma(('turma' + str(i)), 'Ensino Médio', segmentosEnsino[0].cursos[i], '2024', [], [professores[i]], [disciplinas[i]])
        turmas.append(turmaX)
        print(turmaX)
    else:
        turmaX = Turma(('turma' + str(i)), 'Ensino Superior', segmentosEnsino[1].cursos[i-3], '2024', [], [professores[i]], [disciplinas[i]])
        turmas.append(turmaX)
        print(turmaX)


#ALUNOS ==================================================================================================================================================
for i in range(5):
    alunosTemporario = []
    for j in range(20):
        if i < 3:
            alunoX = Aluno(('aluno' + str(i) + '-' + str(j)), (str(i) + '-' + str(j)), ('endereco' + str(i) + '-' + str(j)), ('cpf' + str(i) + '-' + str(j)), ('aln' + str(i) + '-' + str(j)), ('aln.' + str(i) + '-' + str(j) + '@gmail.com'), ('aln.' + str(i) + '-' + str(j)), turmas[i], (str(i) + '-' + str(j)), ('pai.' + str(i) + '-' + str(j)), (str(i) + '-' + str(j)), segmentosEnsino[0].segmento)
            alunos.append(alunoX)
            alunosTemporario.append(alunoX)
            print(alunoX)
        else:
            alunoX = Aluno(('aluno' + str(i) + '-' + str(j)), (str(i) + '-' + str(j)), ('endereco' + str(i) + '-' + str(j)), ('cpf' + str(i) + '-' + str(j)), ('aln' + str(i) + '-' + str(j)), ('aln.' + str(i) + '-' + str(j)), ('aln.' + str(i) + '-' + str(j) + '@gmail.com'), turmas[i], (str(i) + '-' + str(j)), '', (str(i) + '-' + str(j)), segmentosEnsino[1].segmento)
            alunos.append(alunoX)
            alunosTemporario.append(alunoX)
            #print(alunoX)

    turmas[i].alunos = alunosTemporario

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
print(turmas[3].alunos[2])
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
        crudTurma(turmas, alunos, professores, disciplinas, segmentosEnsino)
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