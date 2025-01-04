#agora o professor quer sortear a ordem de apresentação dos trabalhos

from random import shuffle

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

la = [a1,a2,a3,a4]
shuffle(la)
print('A lista de apresentação é {}'.format(la))
