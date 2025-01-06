#distancia em km e calcule a passagem 0.50 p km até 200km e 0.45 p km acima de 200km

num = int(input('Qual a distância da viagem em KM? '))
if num <= 200:
    valor = num * 0.50
    print(f'O valor da viagem é de R${valor}.')
if num > 200:
    valor = num * 0.45
    print(f'O valor da viagem é de R${valor}.')
