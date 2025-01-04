#mostrar parte inteira de um numero real
import math
from math import trunc

num = float(input('Digite um número: '))
print('A parte inteira de {} é {}!'.format(num, math.trunc(num)))