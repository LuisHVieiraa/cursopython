#escreva a velocidade de um carro  / se ultrapassar 80km/h é para aparecer que foi multado / multa de R$7.00 p km acima do limite

v = int(input('Velocidade do carro: '))
vm = 80
if v > vm:
    multa = (v - vm) * 7
    print(f"O carro foi multado em R${multa} por estar {v-vm}Km acima do limite da via")
else:
    print(f'Veículo não foi multado! Está abaixo do limite da via de {vm}KM/h')