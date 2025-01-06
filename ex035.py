#ler comprimento de 3 retas e fale se elas podem ou não formar um triãngulo

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da última reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print(f'As retas {reta1}, {reta2}, {reta3} formam um triângulo!')
else:
    print(f'As retas {reta1}, {reta2}, {reta3} não formam um triângulo!')
