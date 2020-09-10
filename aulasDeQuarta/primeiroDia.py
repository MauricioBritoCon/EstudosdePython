'''felipe.martinelli@professores.unimetrocamp.edu.br
'''

import math
raio = float(input('Digite o valor do raio do circulo: '))

area = math.pi * (raio ** 2)
print(f'A área do seu circulo é de: {area:.3f}')

nota1 = float(input('Digite a primera nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média ficou em: {media}')


nome = str(input('Qual o seu nome? '))
cidade = str(input('Qual a sua cidade? '))
idade = str(input('Qual a sua idade? '))

print(f'Muito bem {nome} você tem apenas {idade} anos e mora na linda cidade de {cidade}.')
print("Olá!", nome, "Sua cidade é", cidade, "e você tem", idade, "anos")


a = 5
b = 6
c = a * b
d = c - (a - b)
print(f'O valor de d é {d}')