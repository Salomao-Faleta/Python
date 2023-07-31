#  #AQUI ESTÃO TOFDOS OS EXERCICÍOS DE PYTHON (@CURSOEMVIDEO)



# #EXERCICÍO 5
# numero = int(input('Digite um número'))
# print('O sucessor de {} é {} o antecessor é {}'.format(numero, numero + 1, numero - 1))


# #EXERCICÍO 6
# numero = int(input('Digite um número'))
# print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(numero, numero * 2, numero * 3, numero ** (1/2)))

# #EXERCICÍO 7
# media1 = float(input('Qual a sua média? '))
# media2 = float(input('Qual a sua média? '))
# print('A média entre {} e {} é {}'.format(media1, media2, (media1 + media2) / 2))



# #USANDO MÓLUDOS DO PYTHON



# #EXERCICÍO 16
# import math
# numero = float(input('Digite um número: '))
# print('A parte inteira de {} é {}'.format(numero, float(numero)))



# #EXERCÍCIO 17
# import math


#     #FORMA MATEMÁTICA
# oposto = float(input('Qual o comprimentpo do Cateto Oposto?'))
# Adjacente = float(input('Qual o comprimentpo do Cateto Adjacente?'))
# hipotenusa = (oposto ** 2 + Adjacente ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

#     #FORMA COM MÓDULOS
# oposto = float(input('Qual o comprimentpo do Cateto Oposto?'))
# Adjacente = float(input('Qual o comprimentpo do Cateto Adjacente?'))
# hipotenusa = math.hypot(oposto, Adjacente)
# print(hipotenusa)




# #Exercício 18

# from math import radians, sin, cos, tan
# #importanto apenas as funções que eu preciso 

# ângulo = float(input('Digite um ângulo: '))

# seno = sin(radians(ângulo))
# print('O ângulo de {:.1f} tem {:.2f}'. format(ângulo, seno))

# cosseno = cos(radians(ângulo))
# print('O cosseno de {:.1f} tem {:.2f}'. format(ângulo, cosseno))

# tangente = tan(radians(ângulo))
# print('O tangente de {:.1f} tem {:.2f}'. format(ângulo, tangente))


# #Exercício 19

# import random

# aluno1 = input('Digite um aluno: ')
# aluno2 = input('Digite um aluno: ')
# aluno3 = input('Digite um aluno: ')

# alunos = [aluno1, aluno2, aluno3]
# escolhido = random.choice(alunos)
# print('O aluno escolhido foi: {}'.format(escolhido))


# #Execício 20

# from random import shuffle

# aluno1 = input('Aluno 1: ')
# aluno2 = input('Aluno 2: ')
# aluno3 = input('Aluno 3: ')
# aluno4 = input('Aluno 4: ')

# alunos = [aluno1, aluno2, aluno3, aluno4]
# shuffle(alunos)
# print('A ordem será: ')
# print(alunos)



# #Exercício 21
# #TOCANDO UM MP3 - EU NÃO FIZ :(



# #Exercício 22