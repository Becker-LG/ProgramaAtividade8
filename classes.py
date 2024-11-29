#ARQUIVO DESTINO À CLASSES

#classe aluno em, informática, mecatronica, eletro, aluno superior, pedagogia, ciencias jsjs
#transferencia, alunos s podem cursar os dois, 
class Pessoa:
       def __init__(self, nome, sobrenome, endereco, cpf, nomeUsuario, email, senha):
              self.nome = nome
              self.sobrenome = sobrenome
              self.endereco = endereco
              self.__cpf = cpf
              self.__nomeUsuario = nomeUsuario
              self.__email = email
              self.__senha = senha

       @property
       def cpf(self):
              return self.__cpf
       @cpf.setter
       def cpf(self, novo):
              self.__cpf = novo

       @property
       def nomeUsuario(self):
              return self.__nomeUsuario
       @nomeUsuario.setter
       def nomeUsuario(self, novo):
              self.__nomeUsuario = novo
       
       @property
       def email(self):
              return self.__email
       @email.setter
       def email(self, novo):
              self.__email = novo
       
       @property
       def senha(self):
              return self.__senha
       @senha.setter
       def senha(self, novo):
              self.__senha = novo

       def __str__(self):
              return f'''
Nome: {self.nome}
Sobrenome: {self.sobrenome}
Endereço: {self.endereco}
CPF: {self.__cpf}
Usuário: {self.__nomeUsuario}
Email: {self.__email}
Senha: {self.__senha}'''

#aluno fechou ==
class Aluno(Pessoa):
       def __init__(self, nome, sobrenome, endereco, cpf, nomeUsuario, email, senha, turma, filiacao, emailResponsavel, registroAcad, segmentoEnsino):
              super().__init__(nome, sobrenome, endereco, cpf, nomeUsuario, email, senha)
              self.turma = turma
              self.filiacao = filiacao 
              self.__emailResponsavel = emailResponsavel
              self.registroAcad = registroAcad
              self.segmentoEnsino = segmentoEnsino

       @property
       def emailResponsavel(self):
              return self.__emailResponsavel
       @emailResponsavel.setter
       def emailResponsavel(self, novo):
              self.__emailResponsavel = novo

       def __str__(self):
              return f'''
{super().__str__()}
Turma: {self.turma.nome}
Filiação: {self.filiacao}
Email Responsável: {self.__emailResponsavel}
Registro Acadêmico: {self.registroAcad}
Segmento de Ensino: {self.segmentoEnsino}'''
       

#professor fechou ==
class Professor(Pessoa):
       def __init__ (self, nome, sobrenome, endereco, cpf, nomeUsuario, email, senha, turma, formacao, disciplinas, segmentos):
              super().__init__(nome, sobrenome, endereco, cpf, nomeUsuario, email, senha)
              self.turma = turma
              self.formacao = formacao
              self.disciplinas = disciplinas
              self.segmentos = segmentos

       def __str__(self):
              return f'''
{super().__str__()}
Turmas: {self.turma}
Formação: {self.formacao}
Disciplinas: {self.disciplinas}
Segmentos de Ensino: {self.segmentos}'''

#ensino médio fechou ==
class EnsinoMedio:
       def __init__(self, cursos):
              self.cursos = cursos

#superior fechou ==
class Superior:
       def __init__(self, cursos):
              self.cursos = cursos

#turmas fechou ==
class Turma:
       def __init__(self, nome, segmentoEnsino, opcaoCurso, anoEscolar, alunos, professores, disciplinas):
              self.nome = nome
              self.segmentoEnsino = segmentoEnsino
              self.opcaoCurso = opcaoCurso
              self.anoEscolar = anoEscolar
              self.alunos = alunos
              self.professores = professores
              self.disciplinas = disciplinas

       def __str__(self):
              return f'''
Nome: {self.nome}
Segmento de Ensino: {self.segmentoEnsino}
Opção de Curso: {self.opcaoCurso}
Ano Escolar: {self.anoEscolar}
Alunos: {len(self.alunos)}
Professores: {len(self.professores)}
Disciplinas: {len(self.disciplinas)}'''

#disciplinas fechou ==
class Disciplinas:
       def __init__(self, id, descricao, segmento, professorTitular):
              self.__id = id
              self.__descricao = descricao
              self.__segmento = segmento
              self.professorTitular = professorTitular

       @property
       def id(self):
              return self.__id
       @id.setter
       def id(self, novo):
              self.__self = novo
       
       @property
       def descricao(self):
              return self.__descricao
       @descricao.setter
       def descricao(self, novo):
              self.__descricao = novo

       @property
       def segmento(self):
              return self.__segmento
       
       def __str__(self):
              return f'''
ID: {self.__id}
Descrição: {self.__descricao}
Segmento de Ensino: {self.__segmento}
Professor Titular: {self.professorTitular}'''