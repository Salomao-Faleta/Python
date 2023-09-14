#  #AQUI ESTÃO TOFDOS OS EXERCICÍOS DE PYTHON (@CURSOEMVIDEO)



# #Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

# numero = int(input('Digite um número'))
# print('O sucessor de {} é {} o antecessor é {}'.format(numero, numero + 1, numero - 1))



# #Exercício Python 06: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# numero = int(input('Digite um número'))
# print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(numero, numero * 2, numero * 3, numero ** (1/2)))



# #Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# media1 = float(input('Qual a sua média? '))
# media2 = float(input('Qual a sua média? '))
# print('A média entre {} e {} é {}'.format(media1, media2, (media1 + media2) / 2))



# #USANDO MÓLUDOS DO PYTHON



# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# import math
# numero = float(input('Digite um número: '))
# print('A parte inteira de {} é {}'.format(numero, float(numero)))




# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.


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




# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# from math import radians, sin, cos, tan
# #importanto apenas as funções que eu preciso 

# ângulo = float(input('Digite um ângulo: '))

# seno = sin(radians(ângulo))
# print('O ângulo de {:.1f} tem {:.2f}'. format(ângulo, seno))

# cosseno = cos(radians(ângulo))
# print('O cosseno de {:.1f} tem {:.2f}'. format(ângulo, cosseno))

# tangente = tan(radians(ângulo))
# print('O tangente de {:.1f} tem {:.2f}'. format(ângulo, tangente))




# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# import random

# aluno1 = input('Digite um aluno: ')
# aluno2 = input('Digite um aluno: ')
# aluno3 = input('Digite um aluno: ')

# alunos = [aluno1, aluno2, aluno3]
# escolhido = random.choice(alunos)
# print('O aluno escolhido foi: {}'.format(escolhido))



# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


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



'''
    Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

    – O nome com todas as letras maiúsculas e minúsculas.

    – Quantas letras ao todo (sem considerar espaços).

    – Quantas letras tem o primeiro nome.
'''

# nome = input('Digite seu nome: ').strip()
# print('Analisando seu nome...')

# print('Seu nome em maiscúlas é {}'.format(nome.upper()))
# print('Seu nome em minuscúlas é {}'.format(nome.lower()))
# print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

# #forma1
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# #forma2
# separa = nome.split()
# print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

'''
    Funcções ultilizadas:
    upper() - Deixa todo o textgo em maiúculas
    lower() - Deixa todo o textgo em maiúculas
    len() - retorna o tamando o texto
    find('alguma coisa') - retorna a posição do que foi passado dentro das aspas 
    o strip elimina os espaços antes e dps de cada texto
    
'''




#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# num = int(input('Informe um número: '))
# print('Analisando o número {}'.format(num))

# unidade = num // 1 % 10 
# dezena = num // 10 % 10 
# centena = num // 100 % 10
# milhar = num // 1000 % 10


# print('Unidade: {}'.format(unidade))
# print('Dezena: {}'.format(dezena))
# print('Centena: {}'.format(centena))
# print('Milhar: {}'.format(milhar))




#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

# cidade = input('Em que cidade voçê nasceu? ').strip()
# print(cidade[:5].upper() == 'SANTO')





#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# nome = input('Qual seu nome completo? ').strip()

# print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))




#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


# frase = str(input('Digite uma frase: ')).upper().strip()
# print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
# print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))

'''
    FUNÇÕES ULTILIZADAS:
        count - Conta quantas vezes algo aparece na frase 
        find - diz a posição onde aparece o que foi passado dentro dos (parênteses)
        rfind - faz a mesma coisa que o find, porém começando do lado direito
'''



#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# n = str(input('Qual seu nome completo? ')).strip()
# nome = n.split()

# print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome)-1]))

'''
    O SPLIT recorta a frase, e podemos pegar cada palvra como array
'''



    #Exercício Python 28: Escreva um programa que faça o computador “pensar”.     
#Em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.



# from random import randint
# from time import sleep

# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
# print('-=-' * 20)
# computador = randint(0,5)

# Jogador = int(input('Em que número eu pensei?'))
# print('PROCESSANDO...')
# sleep(3)

# if Jogador == computador:
#     print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, Jogador))
# else:
#     print('VOCÊ PERDEU!!! eu pensei no número {}, você digitou {}'.format(computador, Jogador))

'''
    FUNÇÕES ULTILIZADAS:
    randint() - gera um número aleatório
    sleep() - dar um tempo para iniciar o que vem dps dela
'''



#   Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

# velocidade = int(input('Qual foi a velocidade atual do carro? '))

# multa = (velocidade - 80) * 7

# if velocidade < 80:
#     print('Tenha um bom dia! E dirija com segurança!')
# else: 
#     print('MULTADO! Você exedeu o limite permitido que é de 80 KM/K. Você deve pagar uma multa de R${} reais.'.format(multa))



#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# numero = int(input('Digite um número: '))

# if numero % 2:
#     print('O número {} é ímpar'.format(numero))
# else:
#     print('O número {} é Par'.format(numero))

'''
    % - Resto da divisão
    TODO NÚMERO PAR DAR RESULTADO = 0
    TODO NÚMERO ÍMPAR DAR RESULTADO = 1
'''



#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# viajem = float(input('Qual a distância da sua viajem ' ))
# print('Você está prestes a começar uma viajem de {:.1f} km'.format(viajem))

# if viajem < 200:
#     print('E o preço da sua passagem será de R${:.2f} reais'.format(viajem * 0.50))
# else:
#     print('E o preço da sua passagem será de R${:.2f} reias'.format(viajem * 0.45))



#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# from datetime import date

# ano = int(input('Que ano quer analisar? E coloque 0 para analisar o ano atual: '))

# if ano == 0:
#     ano = date.today().year
# if(ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0):
#     print('O ano {} é BISSEXTO'.format(ano))
# else:
#     print('O ano {} NÂO é BISSEXTO'.format(ano))



#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


# numero1 = int(input('Primeiro valor: '))
# numero2 = int(input('Segundo valor: '))
# numero3 = int(input('Terceiro valor: '))

# menor = numero1

# if numero2 < numero1 and numero2 < numero3:
#     menor =  numero2
# if numero3 < numero1 and numero3 < numero2:
#     menor = numero3
# #verificando quem é o menor número
# print('O menor número é {}'.format(menor))


# #verificando quem é o maior número

# maior = numero1

# if numero2 > numero1 and numero2 > numero3:
#     maior = numero2
# if numero3 > numero2 and numero3 > numero2:
#     maior = numero3

# print('O maior número é {}'.format(maior))



    #Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# salario = float(input('Quanto você ganha? R$'))

# if salario >= 1250.00:
#     print('Parabéns! Você teve um aumento de 10% que é R${:.2f}'.format(salario * 110/100))
# else:
#     print('Parabés! Você teve um aumento de 15%, que é R${:.2f}'.format(salario * 115/100))



'''
    Exercício Python 35: Desenvolva um programa que leia o 
    comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
# print('-='*20)
# print('Analisador de triângulos ')
# print('-='*20)

# r1 = float(input('Primeiro Segmento: '))
# r2 = float(input('Segundo Segmento: '))
# r3 = float(input('Terceiro Segmento: '))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os segmentos podem formar um triângulo')
# else:
#     print('Os segmentos NÂO podem formar um triângulo')









#==============================================================================================================
#Exercícios fora do curso em vídeo - fonte: https://wiki.python.org.br/EstruturaDeDecisao


'''
    1. Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite um número:'))

if numero1 > numero2:
    print('{} é maior que número {}'.format(numero1, numero2))

'''

'''
    2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input('Digite um valor:'))

if numero >= 0:
    print('{} é positivo'.format(numero))
else:
    print('{} é negativo'.format(numero))

'''

'''
    3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo = str(input('Digite seu sexo? M ou F: '))

if sexo == 'F' or sexo == 'f':
    print('Seu sexo é F - Feminino')
elif sexo == 'M' or sexo == 'm':
    print('Seu sexo é M - Masculino')
else:
    print('Por favor, digite um sexo válido')
'''