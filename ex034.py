#ler salario e calcular aumento / + de 1250 aumento em 10% / menor ou igual a 1250 aumento em 15%

salario = float(input('Digite o salário atual: '))

if salario > 1250.00:
    bon = (salario * 0.10)
    ns = salario + bon
    print(f'O salário atual de R${salario} com o aumento de 10% equivalente a R${bon}\n'
          f'O novo salário passa a ser de R${ns}')

elif salario <= 1250.00:
    bon = (salario * 0.15)
    ns = salario + bon
    print(f'O salário atual de R${salario} com aumento de 15% equivalente a R${bon}\n'
          f'O Novo salário passa a ser de R${ns}')