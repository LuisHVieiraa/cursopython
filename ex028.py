#fazer o computador pensar num numero inteiro entre 0 e 5 e peça para o usuário tentar adivinhar, o programa devera dizer se o usuário adivinhou ou errou

from random import randrange

n = randrange(0,6)
numuser = int(input("Escolha um numero de 0 a 5: "))
if 0 <= numuser <= 5:
    if numuser == n:
        print('Você Acertou! Parabéns!')
    else:
        print(f'Você errou! o número sorteado foi {n}!')

else:
    print(f'O valor {numuser} não está entre 0 e 5!')