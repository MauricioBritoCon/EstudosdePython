import random

reta1 = float(input("Digite o tamanho do primeiro segmento: "))
reta2 = float(input("Digite o tamanho do segundo segmento: "))
reta3 = float(input("Digite o tamanho do terceiro segmento: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos fazem um triangulo")
else:
    print("Os segmentos nao fazem um triangulo")

salario = float(input("Digite o valor do salario"))

if salario >= 1250:
    print(f"O seu salario com aumento é R${salario + (salario * 0.10)}")
else:
    print(f"O seu salario com aumento é R${salario + (salario * 0.15)}")


n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))
n3 = int(input("Digite o terceiro numero"))

if n1 < n2 < n3:
    print(f"O maior numero é {n3} e o menor é {n1}")
elif n2 < n1 <n3:
    print(f"O maior numero é {n3} e o menor é {n1}")
elif n3 < n2 < n1:
    print(f"O maior numero é {n1} e o menor é {n3}")
elif n3 < n1 < n2 :
    print(f"O maior numero é {n2} e o menor é {n3}")

ano = int(input("Digite o ano que voce gostaria de saber se é bissexto"))

if ano % 4 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")

distancia = int(input("Digite a distancia da sua viagem em km"))

if distancia <= 200:
    preco = distancia * 0.50
    print(f"O preço da sua viagem é de R${preco}")
else:
    preco = distancia * 0.45
    print(f"O preço da sua viagem é de R${preco}")

parimpar = int(input("Digite o numero que voce deseja saber se é par ou impar"))

if parimpar % 2 == 0:
    print(f"O numero {parimpar} é par")
else:
    print(f"O numero {parimpar} é impar")

velocidade = int(input("Digite a velocidade que você estava na pista"))

if velocidade >= 80:
    multiplicador = velocidade - 80
    print(f"Você acaba de receber uma multa de R${multiplicador * 7} me passa seu zap")
else:
    print("Você me da pena por viver dentro da lei eu não quero seu zap")
numero = random.randint(0,5)
print(numero)
tentativa = int(input("Tente adivinha o numero em que estou pensando"))

if numero == tentativa:
    print("O numero esta certo você acertou")
else:
    print("Você infelizmente errou o numero meu caro")