#ler frase e mostre quantos "a" tem/em que posição aparece na 1° vez / em que posição aparece na ultima vez

frase = input("Digite uma frase: ")
verif = frase.upper()
vezesa = verif.count('A')
primeiravez = verif.find('A')+1
ultimavez = verif.rfind('A')+1
print('Na frase {}: \n Aparece "A" {}x vezes. \n Aparece pela primeira vez na posição {}.\n Aparece pela ultima vez na posição {}.'.format(frase,vezesa,primeiravez,ultimavez))