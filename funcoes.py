#ARQUIVO DESTINADO À FUNÇÕES

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
def crudTurma(turmas):
    x = 0
    while x == 0:
        print('O que você deseja realizar com a turma?')
        print('''
    Para IMPRIMIR, digite "imprimir";
    Para INSERIR algum estudante, digite "inserir";
    Para EDITAR alguma turma, digite "editar";
    Para DESATIVAR alguma turma, digite "desativar";
    Para EXCLUIR alguma turma, digite "excluir";
    Para SAIR, digite "sair".''')
        entrada = input('')

        if entrada.upper() == "IMPRIMIR":
            print(f'''
Qual turma você deseja imprimir?
No momento possuímos {len(turmas)}, sendo:''')
            for i in range(len(turmas)):
                print(f'{i+1}ª turma: {turmas[i].opcaoCurso}')
            escolha = (f'Digite um número entre 1 e {len(turmas)} para escolher a turma: ')
            


            continue
        elif entrada.upper() == "INSERIR":
            print('')
            continue
        elif entrada.upper() == "EDITAR":
            print('')
            continue
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