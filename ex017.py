# comp cateto oposto/adjascente de um triângulo retângulo e mostre o comprimento da hipotenusa
import math
from math import sqrt, pow

x = float(input('Qual é o comprimento do cateto oposto?'))
y = float(input('E do adjascente? '))

print("A hipotenusa de um Triângulo Retângulo com o Cateto oposto {} e o cateto adjascente {} é {:.2f}".format(x,y,math.hypot(x,y)))
