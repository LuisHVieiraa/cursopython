#area e tinta necessária
lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))

print('A área da parede é de {:.1f}m2 e será necessário de {:.1f} litros de tinta para pinta-la'.format(lar*alt, (lar*alt)/2))