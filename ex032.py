#ler nano e veja se ele é bissexto

ano = int(input("Digite um ano: "))
bissexto = ano % 4
if bissexto == 0:
    print(f'O ano {ano} é um ano bissexto!')
else:
    print(f'O ano {ano} não é um ano bissexto!')