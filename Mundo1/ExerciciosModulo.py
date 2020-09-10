import math
import random


angulo = float(input("Angulo desejado: "))

seno = math.sin(math.radians(angulo))

cos = math.cos(math.radians(angulo))

tan = math.tan(math.radians(angulo))

print(f"O cosseno é {cos} e o seno é {seno} e a tangente {tan}. \n")

alunos = ["huguinho", "zezinho", "pedrinho"]
for nomes in alunos:
    print(nomes)
print(f"O escolhido foi {random.choice(alunos)}.\n")
random.shuffle(alunos)
print(f"A ordem de apresentação é {alunos}.\n")


x = float(input("Digite um numero: "))

print(math.floor(x))

catetoAdj = float(input("Digite o cateto adjacente"))

catetoOps = float(input("Digite o cateto oposto"))

hipotenusa = math.sqrt(math.pow(catetoAdj, 2) + math.pow(catetoOps, 2))

print(f"A hipotenusa deste triangulo retangulo é {hipotenusa}.")
