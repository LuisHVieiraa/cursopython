#tabuáda

n = int(input('Digite um número para calcular sua tabuáda: '))
tab = 0
print('='*20)
print('A tábuada de {} é: '.format(n))
print('='*20)

while(tab <=10):
    print('{} x {:2} = {}'.format(n,tab,n*tab))
    tab = tab + 1
