#ARQUIVO DESTINO À CLASSES

class Pessoa:
       def __init__(self, nome, sobrenome, endereco, cpf, nomeUsuario, email, senha, ativo):
              self.nome = nome
              self.sobrenome = sobrenome
              self.endereco = endereco
              self.__cpf = cpf
              self.__nomeUsuario = nomeUsuario
              self.__email = email
              self.__senha = senha
              self.ativo = ativo

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
Senha: {self.__senha}
ativo: {self.ativo}'''

#aluno fechou ==
class Aluno(Pessoa):
       def __init__(self, nome, sobrenome, endereco, cpf, nomeUsuario, email, senha, ativo, turma, filiacao, emailResponsavel, registroAcad, segmentoEnsino):
              super().__init__(nome, sobrenome, endereco, cpf, nomeUsuario, email, senha, ativo)
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
Turma: {len(self.turma)}
Filiação: {self.filiacao}
Email Responsável: {self.__emailResponsavel}
Registro Acadêmico: {self.registroAcad}
Segmento de Ensino: {self.segmentoEnsino}'''
       

#professor fechou ==
class Professor(Pessoa):
       def __init__ (self, nome, sobrenome, endereco, cpf, nomeUsuario, email, senha, ativo, turmas, formacao, disciplinas, segmentos):
              super().__init__(nome, sobrenome, endereco, cpf, nomeUsuario, email, senha, ativo)
              self.turmas = turmas
              self.formacao = formacao
              self.disciplinas = disciplinas
              self.segmentos = segmentos

       def __str__(self):
              return f'''
{super().__str__()}
Turmas: {len(self.turmas)}
Formação: {self.formacao}
Disciplinas: {len(self.disciplinas)}
Segmentos de Ensino: {len(self.segmentos)}'''

#segmento de ensino
class SegmentoEnsino:
       def __init__(self, segmento, cursos, ativo):
              self.segmento = segmento
              self.cursos = cursos
              self.ativo = ativo

#turmas fechou ==
class Turma:
       def __init__(self, nome, segmentoEnsino, opcaoCurso, anoEscolar, alunos, professores, disciplinas, ativo):
              self.nome = nome
              self.segmentoEnsino = segmentoEnsino
              self.opcaoCurso = opcaoCurso
              self.anoEscolar = anoEscolar
              self.alunos = alunos
              self.professores = professores
              self.disciplinas = disciplinas
              self.ativo = ativo

       def __str__(self):
              return f'''
Nome: {self.nome}
Segmento de Ensino: {self.segmentoEnsino}
Opção de Curso: {self.opcaoCurso}
Ano Escolar: {self.anoEscolar}
Alunos: {len(self.alunos)}
Professores: {len(self.professores)}
Disciplinas: {len(self.disciplinas)}
Ativo: {self.ativo}'''

#disciplinas fechou ==
class Disciplina:
       def __init__(self, id, descricao, segmento, professorTitular, ativo):
              self.__id = id
              self.__descricao = descricao
              self.__segmento = segmento
              self.professorTitular = professorTitular
              self.ativo = ativo

       @property
       def id(self):
              return self.__id
       @id.setter
       def id(self, novo):
              self.__id = novo
       
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
Professor Titular: {self.professorTitular}
Ativo: {self.ativo}'''