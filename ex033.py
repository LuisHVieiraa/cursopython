# ler 3 numeros e mostrar qual é o menor e o maior

num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite o último número: '))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print(f'Entre os números {num1},{num2} e {num3}\n O maior número é {maior} e o menor número é {menor}.')