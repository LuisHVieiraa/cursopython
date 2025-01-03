#15% de aumento no salário

s = float(input('Qual é seu salário atual? '))
b = (15/100) * s
ns = s + b

print('Seu salário é de {:.2f}, com a bonificação de 15% seu salário aumentou {:.2f} reais'.format(s,b))
print('Seu novo salário é de {:.2f} reais'.format(ns))