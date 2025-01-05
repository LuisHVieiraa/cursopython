#ler num de 0 a 9999 e mostre cada um dos digitos separados

num = input("Digite um número de 0 a 9999: ").zfill(4)
lista = list(num)

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(lista[3], lista[2], lista[1], lista[0]))
