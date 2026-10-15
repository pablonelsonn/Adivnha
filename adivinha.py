#Projetinho de estudo de Python
import random

numero_minimo = int(input('Qual será o número mínimo do intervalo?\n'))
numero_maximo = int(input('Qual será o número máximo do intervalo?\n')) 

tentativas = int(input('Quantas tentativas você quer ter?\n'))

numero_asorte = random.randint(numero_minimo, numero_maximo)

while True:
    tentativa = int(input(f'Digite o número entre {numero_minimo} e {numero_maximo}. \n'))

    if tentativa  == numero_asorte:
        print('Parabéns! Você acertou o número!')
        break