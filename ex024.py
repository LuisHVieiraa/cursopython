#ler nome e ve se começa com santo ou não

nome = input('Nome: ').strip().upper().split()
print('SANTO' in nome[0])