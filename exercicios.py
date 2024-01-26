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

'''
    Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
    Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

# casa = float(input('Valor da casa: R$'))
# salario = float(input('Salário do comprador: R$'))
# anos = int(input('Em quantos anos de financiamneto? '))
# prestação = casa / (anos * 12)
# minimo = salario * 30 / 100
# print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))

# if prestação <= minimo:
#     print('Empréstimo pode ser concedido!')
# else:
#     print('Empréstimo NEGADO!')



'''
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário,
 escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.
'''


# num = int(input('Digite número inteiro: '))
# print('''
# [ 1 ] - Converter para BINÁRIO
# [ 2 ] - Converter para OCTAL
# [ 3 ] - Converter para HEXADECIMAL''')
# opçao = int(input('Sua opção: '))


# if opçao == 1:
#     print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
# elif opçao == 2:
#     print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
# elif opçao == 3:
#     print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
# else:
#     print('Digite uma opção válida')


'''
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. 
mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''

# numero1 = int(input('Primerio número '))
# numero2 = int(input('Segundo número '))

# if numero1 > numero2:
#     print('O primeiro é maior'.format(numero1))
# elif numero2 > numero1:
#     print('O Segundo é maior'. format(numero2))
# else:
#     print('Não existe valor maior, os dois são iguais')


'''
    Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
    de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
    se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# '''

# from datetime import date
# atual = date.today().year

# nascimento = int(input('Ano de nascimento: '))
# idade = atual - nascimento
# print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual ))


# if idade == 18:
#     print('Deve se alistar IMEDIATAMENTE!!!')
# elif idade < 18:
#     saldo = 18 - idade
#     print('Ainda faltam {} anos para seu alistamento'.format(saldo))
# else:
#     saldo = idade - 18
#     print('Você já deveria ter se alistado há {} anos'.format(saldo))

'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

'''

# media1 = float(input('Primeira nota: '))
# media2 = float(input('Segunda nota: '))
# resulatdo = (media1 + media2) / 2

# if resulatdo < 5:
#     print('A média do aluno foi {}, e ele está REPROVADO!'.format(resulatdo))
# elif resulatdo >= 5 and resulatdo <= 6.9:
#     print('A média do aluno foi {}, e ele está em RECUPERAÇÃO!!'.format(resulatdo))
# else:
#     print('A média do aluno foi {}, e ele foi APROVADO!!!'.format(resulatdo))


'''
    Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
    de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER

'''

# from datetime import date
# atual = date.today().year

# nascimento = int(input('Qual seu ano de nascimento? '))
# idade = atual - nascimento
# print('O atleta tem {} anos'.format(idade))

# if idade <= 9:
#     print('Classificação: MIRIM')
# elif idade > 9 and idade <= 14:
#     print('Classificação: INFANTIL')
# elif idade > 14 and idade <= 19:
#     print('Classificação: JÚNIOR')
# elif idade > 19 and idade <= 25:
#     print('Classificação: SÊNIOR')
# else:
#     print('Classificação: MASTER')


'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de 
triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''


# r1 = float(input('Primeiro Segmento: '))
# r2 = float(input('Segundo Segmento: '))
# r3 = float(input('Terceiro Segmento: '))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os segmentos podem formar um triângulo', end=' ')

#     if r1 == r2 and r2 == r3:
#         print('EQUILÁTERO')

#     elif r1 != r2 and r2 != r3 and r3 != r1:
#         print('ESCALENO')
    
#     else:
#         print('ISÓLECES')


# else:
#     print('Os segmentos NÂO podem formar um triângulo')

'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''

# peso = float(input('Qual seu peso? (Kg) '))
# altura = float(input('Qual é sua altura (m)'))
# # dividimos o peso pela altura ao quadrado
# imc = peso / (altura ** 2)
# print('O IMC é de ${:.1f}'.format(imc))


# if imc < 18.5:
#     print('Você está ABAIXO DO PESO')
# elif imc >= 18.5 and imc < 25:
#     print('Você está no PESO IDEAL')
# elif imc >= 25 and imc < 30:
#     print('Você está em SOBREPESO')
# elif imc >= 30 and imc < 40:
#     print('Você está na OBESIDADE')
# else:
#     print('Você está na OBESIDADE MÓRBIDA')




'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

# '''

# valorCompra = float(input('Qual o valor das comprar? R$'))
# print('FORMAS DE PAGAMENTO')
# print('[1] - à vista dinheiro/cheque: 10%')
# print('[2] – à vista no cartão: 5% de desconto')
# print('[3] - em até 2x no cartão: preço normal')
# print('[4] – 3x ou mais no cartão: 20% de juros')
# opcao = int(input('Qual a forma de pagamento?'))


# if opcao == 1:
#     total = valorCompra - (valorCompra * 10 / 100)
# elif opcao == 2:
#     total = valorCompra - (valorCompra * 5 / 100)
# elif opcao == 3:
#     total = valorCompra
#     parcela = valorCompra / 2
#     print('Sua compra foi parcela em 2x de ${:.2f} SEM JUROS'.format(parcela))
# elif opcao == 4:
#     total = valorCompra + (valorCompra * 20 / 100)
#     totalParcelas = int(input('Em quantas parcelas?'))
#     parcela = total / totalParcelas
#     print('Sua compra foi parcela de ${}x de ${:.2f} COM JUROS'.format(totalParcelas, parcela))
# else:
#     total = 0
#     print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')

# print('Sua compra de R$${:.2f} ficou R${:.2f} no final'.format(valorCompra, total))

'''
    Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô (pedra, papel ou tesoura) com você.
'''


# #fazendo a parte para o computador escolher aleatoriamente
# from random import randint
# from time import sleep
# itens = ('pedra', 'papel', 'tesoura')
# computador = randint(0,2)
# # print('o computador escolheu {}'.format(itens[computador])) AQUI SABEMOS OQ O COMPUTADOR ESCOLHEU

# #jogador
# print('''
# SUAS OPÇÕES
# [0] - PEDRA
# [1] - PAPEL
# [2] - TESOURA
# ''')

# jogador = int(input('Qual é sua jogada? '))
# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!!!')

# print('-=' * 20)
# print('Computador jogou {}'.format(itens[computador]))
# print('jogador jogou {}'.format(itens[jogador]))
# print('-=' * 20)


# if computador == 0:
#     if jogador == 0:
#         print('DEU EMPATE!')
#     elif jogador == 1:
#         print('JOGADOR VENCEU!')
#     elif jogador == 2:
#         print('COMPUTADOR VENCEU!')
#     else:
#         print('Jogada inválida')

# elif computador == 1:
#     if jogador == 0:
#         print('COMPUTADOR VENCEU')
#     elif jogador == 1:
#         print('DEU EMPATE!')
#     elif jogador == 2:
#         print('JOGADOR VENCEU!')
#     else:
#         print('Jogada inválida')


# elif computador == 2:
#     if jogador == 0:
#         print('JOGADOR VENCEU!')
#     elif jogador == 1:
#         print('COMPUTADOR VENCEU!')
#     elif jogador == 2:
#         print('DEU EMPATE!')
#     else:
#         print('Jogada inválida')

'''
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de 
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

# from time import sleep

# for c in range(10, -1, -1):
#     print(c)
#     sleep(1)
# print('FELIZZ ANO NOVOOO!!!')


'''
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

# for i in range(2, 51, 2):
#     print(i)
# print('fim')

'''
    Exercício Python 48: Faça um programa que calcule a soma entre todos os números 
    que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

# soma = 0
# for i in range(1,501, 2):
#     if i % 3 == 0:
#         soma += i
# print('A soma dos números solicitados é {}'.format(soma))


'''
    Exercício Python 49: Refaça o DESAFIO 9,
    mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''

# numero = int(input('Digite um número para ver sua tabuada: '))

# for i in range(1, 11):
#     print('{} x {} = {}'.format(numero, i, numero * i))


'''
    Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
    daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

# soma = 0
# cont = 0
# for i in range(1,7):
#     numero = int(input('Digite o {}° valor: '.format(i)))
#     if numero % 2 == 0:
#         soma += numero
#         cont += 1
# print('Você informou {} números pares e a soma foi {}' .format(cont, soma))



'''
    Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
    No final, mostre os 10 primeiros termos dessa progressão.
'''

# print('=' * 20)
# print(' 10 termos de uma PA')
# print('=' * 20)

# primeiroTermo = int(input('Primeiro termo: '))
# razao = int(input('Qual a razão? '))
# decimo = primeiroTermo + (11 - 1) * razao

# for i in range(primeiroTermo, decimo, razao):
#     print(i)
# print('Acabou')

'''
    Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

# num = int(input('Digite um número: '))
# tot = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         print('\033[33m', end="")
#         tot += 1
#     else:
#          print('\033[31m', end=" ")
#     print('{}'.format(i), end=" ")
# print('o numero {} foi divisível {} vezes'.format(num, tot))

# if tot == 2:
#     print('Por isso ele é primo')
# else: 
#     print('Por isso ele não é Primo')


'''
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:
    => APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''

# frase = str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''

# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
# print('O inverso de {} é {}'.format(junto, inverso))
# if inverso == junto:
#     print('Tempos um palímodro')
# else:
#     print('Não temos um palímodro')


'''
    Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
    No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
# from datetime import date
# atual = date.today().year
# totMaior = 0
# totMenor = 0

# for pes in range(1,8):
#     nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pes)))
#     idade = atual - nasc
#     if idade >= 18:
#         totMaior+=1
#     else:
#         totMenor+= 1
# print('Ao todo tivemos {} pessoas maiores de idade'.format(totMaior))
# print('Ao todo tivemos {} pessoas menores de idade'.format(totMenor))


'''
    Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
    No final, mostre qual foi o maior e o menor peso lidos.
'''

# maiorPeso = 0
# menorPeso = 0

# for p in range(1,6):
#     peso = float(input('Qual é o peso da {}° pessoa? '.format(p)))
#     if p == 1:
#         maiorPeso = peso
#         menorPeso = peso
#     else:
#         if peso > maiorPeso:
#             maiorPeso = peso
#         if peso < menorPeso:
#             menorPeso = peso
# print('O maior peso lido foi {}kg'.format(maiorPeso))
# print('O menor peso lido foi {}kg'.format(menorPeso))

'''
    Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
    mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

# somaIdade = 0
# mediaIdade = 0
# maiorIdadeHomem = 0
# nomeVelho = ''
# Mulher20 = 0

# for p in range(1,5):
#     print('----- {}° PESSOA -----'.format(p))
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo: [M/F]: ')).strip()

#     somaIdade += idade


#     if p == 1 and sexo in 'Mm':
#         maiorIdadeHomem = idade
#         nomeVelho = nome
#     if sexo in 'Mn' and idade > maiorIdadeHomem:
#         maiorIdadeHomem = idade
#         nomeVelho = nome
#     if sexo in 'Ff' and idade < 20:
#         Mulher20 += 1

# mediaIdade = somaIdade / 4
# print('A média do grupo é de {} anos'.format(mediaIdade))
# print('O homem mais velo tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))
# print('{} mulheres tem menos de 20 anos'.format(Mulher20))


'''
    Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
    Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

# sexo = input('Qual seu sexo? [M/F]').upper()

# while sexo not in 'MF':
#     print('Digite um sexo VÁLIDO!')
#     print('================================')
#     sexo = input('Qual seu sexo? [M/F]').upper()
    
# print('Obrigado! seu sexo é {}'.format(sexo))

'''
    Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram 
    necessários para vencer.
'''

# from random import randint

# nome = input('Qual seu nome: ').strip()

# computador = randint(0, 11)
# jogador = int(input('Olá {}! Em que número eu pensei?'))
# totVez = 1

# while jogador != computador:
#     print('ERROU! TENTE NOVAMENET')
#     totVez += 1

#     if jogador > computador:
#         print('Experimente um número menor')
#     else:
#         print('Experimente um número maior')
    
#     print('=' * 20)

#     jogador = int(input('Em que númerov eu pensei?'))
# print('Parabéns! você precisou de {} chances para acertar'.format(totVez))


'''
    Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
# from time import sleep

# n1 = int(input('Digite o 1° número '))
# n2 = int(input('Digite o 2° número '))
# opcao = 0

# while opcao != 5:
#     print('''
#     [ 1 ] somar
#     [ 2 ] multiplicar
#     [ 3 ] maior
#     [ 4 ] novos números
#     [ 5 ] sair do programa''')
#     opcao = int(input('>>>>>>>>>>>>O que deseja fazer com os valores? '))

#     if opcao == 1:
#         print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
#     elif opcao == 2:
#         print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
#     elif opcao == 3:
#         if n1 > n2:
#             print('Entre {} e {} o {} é maior'.format(n1, n2, n1))
#         else:
#             print('Entre {} e {} o {} é maior'.format(n2, n1, n2))
#     elif opcao == 4:
#         print('Os novos númeos')
#         n1 = int(input('Digite o 1° valor: '))
#         n2 = int(input('Digite o 2° valor: '))
#     elif opcao == 5:
#         print('Finalizando...')
#         sleep(2)
#     else:
#         print('Digite um valor válido')


# print('Volte sempre!')

'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

#1° forma de fazer
# from math import factorial
# n = int(input('Digite um número para calcular o fatorial'))
# f = factorial(n)
# print('O factorial de {} é {}'.format(n, f))


#2° Forma de fazer
# n = int(input('Digite um número para calcular o fatorial'))
# c = n
# f = 1
# print('calculando {}'.format(n))
# while c > 0:
#     print(' {} '.format(c), end="")
#     print('x' if c > 1 else ' = ', end="")
#     f *= c
#     c -= 1
# print('{}'.format(f))


'''
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''


# print('=' * 20)
# print(' 10 termos de uma PA')
# print('=' * 20)

# primeiroTermo = int(input('Primeiro termo: '))
# razao = int(input('Qual a razão? '))
# termo = primeiroTermo
# cont = 1

# while cont < 11:
#     print('{} => '.format(termo), end="")
#     termo += razao
#     cont += 1
# print('FIM')


'''
    Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
    O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

# print('=' * 20)
# print(' 10 termos de uma PA')
# print('=' * 20)

# primeiroTermo = int(input('Primeiro termo: '))
# razao = int(input('Qual a razão? '))
# termo = primeiroTermo
# cont = 1
# total = 0
# mais = 10

# while mais != 0:
#     total += mais
#     while cont <= total:
#         print('{} => '.format(termo), end="")
#         termo += razao
#         cont += 1
#     print('PAUSA')
#     mais = int(input('Quantos termos você quer mostrar a mais? '))
# print('FIM!')


'''
    Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
    elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
'''

# print('-'* 30)
# print('Sequência de Fibonacci.')
# print('-'* 30)

# n = int(input('Quantos termos voçê quer mostrar? '))

# t1 = 0
# t2 = 1
# print('~'*30)
# print('{} => {}'.format(t1, t2), end="")
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     print(' => {}'.format(t3), end="")
#     t1 = t2
#     t2 = t3
#     cont += 1
# print('=> FIM!')
# print('~'*30)

'''
    Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
    O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
    mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

# n = 0
# cont = 0
# soma = 0
# n = int(input('Digite um número: [999 para parar] '))

# while n != 999:
#     soma += n
#     cont += 1
#     n = int(input('Digite um número: [999 para parar] '))
# print('Você digitou {} números e a soma deles foram {}'.format(cont, soma))
# print('ACABOU!')



'''
    Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''


# resp = 'S'
# soma = quant = media = maior = menor = 0
# while resp in 'Ss':
#     núm = int(input('Digite um número: '))
#     soma += núm
#     quant += 1

#     if quant == 1:
#         maior = menor = núm
#     else:
#         if núm > maior:
#             maior = núm
#         if núm < menor:
#             menor = núm

#     resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
# media = soma / quant
# print('Você digitou {} números e a média dos número foi {}'.format(quant, media))
# print('O maior foi {} e o menor foi {}'. format(maior, menor))


'''
    Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

'''

# numero = int(input('Digite um número (999 para parar): '))
# soma = 0
# num_digitado = 0

# while numero != 999:
#     soma += numero
#     num_digitado += 1
#     numero = int(input('Digite um número (999 para parar): '))
# print(f'A soma dos números é {soma} e vc digitou {num_digitado} números')


'''
    Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, 
    para cada valor digitado pelo usuário. 
    O programa será interrompido quando o número solicitado for negativo.
'''


# while True:
#     print('='*50)
#     numero = int(input('quer ver a tabuada de que valor? '))
    
#     if numero > 0:
#         for i in range(1, 11):
#             print('{} x {} = {}'.format(numero, i, numero * i))
    
#     else:
#         print('NÃO ACEITAMNOS NÚMEROS NEGATIVOS')
#         break
# print('===>SAIU DO LAÇO<===')
