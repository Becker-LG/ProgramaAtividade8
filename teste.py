i = 5
teste = 'teste'

teste2 = teste + str(i)
print(teste2)

from classes import EnsinoMedio

#ensinoMedio = EnsinoMedio(['Mecatrônica', 'Eletromecânica', 'Informática'])
#
#print(ensinoMedio.cursos[0])

ensinos = []
for i in range(3):
    ensinoMedio = EnsinoMedio(['Mecatrônica', 'Eletromecânica', 'Informática'])
    ensinos.append(ensinoMedio)

print(ensinos[2].cursos[2])

ensinoMedio = EnsinoMedio(['Mecatrônica', 'Eletromecânica', 'Informática'])

x = ['teste']
#y = 'teste2'
z = x + list(ensinoMedio)

print(z)

