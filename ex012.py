#novo preço com 5% de desconto

p = float(input('Qual o preço atual do produto? '))
d = int(input('Qual a porcentagem de desconto? '))

d = d/100
print('O preço atual do produto é de {} mas com o desconto passa a ser de {:.2f}'.format(p,p-p*d))