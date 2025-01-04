#sen cos tan de um angulo qualquer

import math

ang = int(input('Digite o ângulo: '))

print('o Ângulo {:.2f} tem o seno {:.2f}, o cosseno {:.2f} e a tanjente {:.2f}!'.format(ang, math.sin(math.radians(ang)),math.cos(math.radians(ang)),math.tan(math.radians(ang))))