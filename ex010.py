#cotação
c = float(input('Quanto tem na carteira? '))
cot = 3.27

print('Cotação atual do Dólar: US$1,00 = {}'.format(cot))
print('Com {} reais você pode comprar {:.2f} dólares'.format(c,c/cot))
