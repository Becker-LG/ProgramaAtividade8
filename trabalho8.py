#classe aluno em, informática, mecatronica, eletro, aluno superior, pedagogia, ciencias jsjs
#transferencia, alunos s podem cursar os dois, 
class Pessoa:
       def __init__(self, nome, sobrenome, endereco, turma, cpf, nomeUsuario, email, senha):
              self.nome = nome
              self.sobrenome = sobrenome
              self.endereco = endereco
              self.turma = turma
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

#aluno fechou ==
class Aluno(Pessoa):
       def __init__(self, nome, sobrenome, endereco, cpf, turma, nomeUsuario, email, senha, filiacao, emailResponsavel, registroAcad, segmentoEnsino):
              super().__init__(nome, sobrenome, endereco, cpf, turma, nomeUsuario, email, senha)
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

#professor fechou ==
class Professor(Pessoa):
       def __init__ (self, nome, sobrenome, endereco, cpf, turma, nomeUsuario, email, senha, formacao, disciplinas, segmentos):
              super().__init__(nome, sobrenome, endereco, cpf, turma, nomeUsuario, email, senha)
              self.formacao = formacao
              self.disciplinas = disciplinas
              self.segmentos = segmentos

#ensino médio fechou ==
class EnsinoMedio(Aluno):
       def __init__(self, mecatronica, eletromecanica, informatica):
              self.mecatronica = mecatronica
              self.eletromecanica = eletromecanica
              self.informatica = informatica

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

#superior fechou ==
class Superior(Aluno):
       def __init__(self, cienciaComputacao, pedagogia):
              self.cienciaComputacao = cienciaComputacao
              self.pedagogia = pedagogia

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