#classe aluno em, informática, mecatronica, eletro, aluno superior, pedagogia, ciencias jsjs
#transferencia, alunos s podem cursar os dois, 

class Aluno:
       def __init__ (self, nome, sobrenome, endereco, filiacao, emailResponsavel, regAcad, segmentoEnsino, turma, nomeUsuario, email, senha):
              self.nome = nome
              self.sobrenome = sobrenome
              self.endereco = endereco
              self.filiacao = filiacao 
              self.__emailResponsavel = emailResponsavel
              self.regAcad = regAcad
              self.segmentoEnsino = segmentoEnsino
              self.turma = turma
              self.__nomeUsuario = nomeUsuario
              self.__email = email
              self.__senha = senha

       @property
       def emailResponsavel(self):
              return self.__emailResponsavel
       
       @property
       def nomeUsuario(self):
              return self.__nomeUsuario
       
       @property
       def email(self):
              return self.__email
       
       @property
       def senha(self):
              return self.__senha

class Professor:
       def __init__ (self, nome, sobrenome, cpf, endereco, formacao, disciplinas, segmentos, turma, nomeUsuario, email, senha):
              self.nome = nome
              self.sobrenome = sobrenome
              self.__cpf = cpf
              self.endereco = endereco
              self.formacao = formacao
              self.disciplinas = disciplinas
              self.segmentos = segmentos
              self.turma = turma
              self.__nomeUsuario = nomeUsuario
              self.__email = email
              self.__senha = senha

       @property
       def cpf (self):
              return self.__cpf
       
       @property
       def nomeUsuario(self):
              return self.__nomeUsuario
       
       @property
       def email(self):
              return self.__email
       
       @property
       def senha(self):
              return self.__senha

class EnsinoMedio(Aluno):
       def __init__(self, eletromecanica, informatica, mecatronica):
              self.eletromecanica = eletromecanica
              self.informatica = informatica
              self.mecatronica = mecatronica

class Turma:
       def __init__(self, nome, segmentoEnsino, opcaoCurso, anoEscolar, alunos, professores, disciplinas):
              self.nome = nome
              self.segmentoEnsino = segmentoEnsino
              self.opcaoCurso = opcaoCurso
              self.anoEscolar = anoEscolar
              self.alunos = alunos
              self.professores = professores
              self.disciplinas = disciplinas

class Superior(Aluno):
       def __init__(self, pedagogia, cienciaComputacao):
              self.pedagogia = pedagogia
              self.cienciaComputacao = cienciaComputacao
       
class Disciplinas:
       def __init__(self, id, descricao, segmento, professorTitular):
              self.__id = id
              self.__descricao = descricao
              self.__segmento = segmento
              self.professorTitular = professorTitular

       @property
       def id(self):
              return self.__id
       
       @property
       def descricao(self):
              return self.__descricao
       
       @property
       def segmento(self):
              return self.__segmento





