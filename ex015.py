#aluguel de carros

d = int(input('quantos dias o veículo ficou alugado? '))
km = float(input('quantos km rodados? '))

preco = (km*0.15) + (d*60)

print('O preço do aluguel do veículo foi de R${}'.format(preco))