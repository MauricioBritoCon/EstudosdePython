'''1- Faça um programa que receba o nome de duas pessoas e dê uma mensagem de boas vindas com o nome delas.
2- Faça um programa que receba o nome, o ano de nascimento de uma pessoa e o ano atual, e mostre uma mensagem com o nome, a idade dessa pessoa e quantos anos ela terá em 2050.
3- Faça um programa que receba 3 notas e 3 pesos, calcule e mostre a média ponderada das notas. Neste caso, o usuário irá inserir tanto as notas quanto o peso que elas possuem dentro da média ponderada.
'''
import math


nota1 = float(input('Digite a primeira nota: '))
peso1 = float(input('Digite o peso da primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
peso2 = float(input('Digite o peso da segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
peso3 = float(input('Digite o peso da terceira nota: '))

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f'Sua média pondera é: {media}')