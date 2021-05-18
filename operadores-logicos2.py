'''
EXERCICIO:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
e decide se ela está apta a ser do exercito.
Para entrar no exercito é preciso ter mais de 18 anos, pesar mais de 60kg
e medir mais ou igual a 1.70 metros.
'''

idade = int(input('Qual a sua idade: '))
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Voce pode entrar no exército!')

else:
    print('Voce não pode entrar no exercito.')
