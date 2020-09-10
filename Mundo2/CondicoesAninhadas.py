import datetime
import random

computador = random.randint(0, 2)
usuario = input("Escolha entre 'pedra' 'papel' 'tesoura': ")
usuario = usuario.lower()
if computador == 0:
    escolha = 'pedra'
elif computador == 1:
    escolha = 'papel'
else:
    escolha = 'tesoura'

if computador == 0 and usuario == 'pedra' or computador == 1 and usuario == 'papel' or computador == 3 and usuario == 'tesoura' :
    print(f"Você empatou pois o computador escolheu {escolha} e você tambem.")
elif computador == 0 and usuario == 'papel' or computador == 1 and usuario == 'tesoura' or computador == 2 and usuario == 'pedra':
    print(f"Você ganhou pois o computador escolheu {escolha} e você {usuario}.")
else:
    print(f'Você perdeu pois escolheu {usuario} e o computador escolheu {escolha}')

preco = float(input("Digite o preço do produto: R$"))
forma = input("Digite a forma de pagamento 'cheque' 'dinheiro' 'cartao' '2xcartao' ou '3x+cartao'")

if forma == 'dinheiro' or forma == 'cheque':
    print(f"O produto vai custar {preco - (preco * 0.10)}")
elif forma == 'cartao':
    print(f"O produto vai custar {preco - (preco * 0.05)}")
elif forma == '2xcartao':
    print(f"O produto vai custar {preco}")
elif forma == '3x+cartao':
    print(f"O produto vai cust {preco + (preco * 0.20)}")
else:
    print("Forma de pagamento invalida")

anoAtual = datetime.datetime.now()

peso = float(input("Digite seu peso em kg: "))
altura = int(input("Digite sua altura cm: "))

imc = peso / ((altura / 100) ** 2)

if imc < 18.5:
    print("Você esta abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Você esta no peso ideal")
elif imc >= 25 and imc < 30:
    print("Você tem sobrepeso")
elif imc >= 30 and imc < 40:
    print("Você tem obesidade")
else:
    print("Voce tem obesidade morbida")

reta1 = float(input(f"Digite o comprimento da primeira reta: "))
reta2 = float(input(f"Digite o comprimento da segunda reta: "))
reta3 = float(input(f"Digite o comprimento da terceira reta: "))

if reta1 + reta2 >= reta3 and reta3 + reta2 >= reta1 and reta3 + reta1 >= reta1:
    if reta1 == reta2 and reta2 == reta3:
        print(f"O triangulo é equilatero")
    elif reta1 == reta2 or reta3 == reta1:
        print(f"Este é um triangulo isósceles tem 2 lados iguais")
    else:
        print("Este triangulo é escaleno")
else:
    print("Estas retas nao fazem um triangulo")
anoNascimento = int(input("Digite aqui o ano do seu nascimento: "))
idade = anoAtual.year - anoNascimento
if idade <= 9:
    print(f"Você tem {idade}anos e pertence aos nadadores mirim")
elif idade <= 14:
    print(f"Você tem {idade}anos e pertence aos nadadores infantis")
elif idade <= 19:
    print(f"Você tem {idade}anos e pertence aos nadadores junior")
elif idade == 20:
    print(f"Você tem {idade}anos e pertence aos nadadores sênior")
else:
    print(f"Você tem {idade}anos e pertence aos nadadores master")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
mediaNota = (nota1 + nota2) / 2

if mediaNota < 5.00:
    print(f"Parabens você foi reprovado com a media {mediaNota}")
elif 5 <= mediaNota <= 6.9:
    print(f"Parabens você esta de recuperação com a media {mediaNota}")
else:
    print(f"Meus pesames você foi aprovado com a media {mediaNota}")

nascimento = int(input("Digite o ano de nascimento: "))

idade = anoAtual.year - nascimento
if idade > 18:
    print(f"Já passou o tempo do seu alistamento em {idade - 18}anos")
elif idade == 18:
    print("Esta na hora de se alistar")
else:
    print(f"Ainda faltam {18 - idade} anos para você se alistar ")

n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))

if n1 > n2:
    print("O primeiro numero é maior")
elif n2 > n1:
    print("O segundo numero é maior")
else:
    print("Ambos são iguais")

opcao = int(input("Digite '1' para converter em binario '2' em octa e '3' em hexa: "))
numero = int(input("Digite um numero que queria converter para binario: "))

if opcao == 1:
    numeroBi = bin(numero)

    print(f"O numero {numero} em binario é: {numeroBi}")
elif opcao == 2:
    numeroOcta = oct(numero)
    print(f"O numero {numero} em octa é: {numeroOcta}")
elif opcao == 3:
    numeroHexa = hex(numero)
    print(f"O numero {numero} em hexa é: {numeroHexa}")
else:
    print("Digite uma opção valida")


valorCasa = float(input("Digite o valor da casa sem ponto: R$"))
salario = float(input("Digite o valor do seu salario: R$"))
tempo = int(input("Em quantos anos quer pagar o emprestimo? "))

valorPrestacao = valorCasa / (tempo * 12)

if valorPrestacao >= (salario * 0.30):
    print("Seu emprestimo não foi aprovado pois o valor mensal supera 30% do seu salario")
    print(f"O valor do seu emprestimo mensal: R${valorPrestacao} e seu salario é R${salario}")
elif valorPrestacao < (salario * 0.30):
    print(f"Seu emprestimo foi aprovado pois o valor de R${valorPrestacao} é menor que 30% de seu salario de R${salario}")
