#ler nome/ mostrar tudo maiusculo / tudo minusculo / quantas letras tem sem considerar espaços/ quantas letras tem o primeiro nome

nome = str(input('Qual seu nome completo? ')).strip()
nomemai = nome.upper()
nomemin = nome.lower()
nomelet = len(nome.replace(" ", ""))
primnome = nome.split()[0]
primnomelet = len(nome.split()[0])

print('Nome Completo: {}.\n Nome tudo em maiúsculo: {}.\n Nome tudo em minúsculo: {}.\n Quantas Letras possui sem espaços: {}.\n Primeiro nome: {} e tem {} letras.'.format(nome,nomemai,nomemin,nomelet,primnome,primnomelet))