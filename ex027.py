#ler nome completo e mostre apenas primeiro e ultimo nome
nome = str(input('Qual seu nome completo? '))

primnome = nome.split()[0]
ultimnome = nome.split()[-1]

print(f'No nome {nome}: \nO primeiro nome é {primnome}\nO ultimo nome é {ultimnome}')