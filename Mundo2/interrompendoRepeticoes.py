import random

import math
n = "abelha"
print(n[1] in 'aeoiu')

resp = str(input("Digite uma letra: ")).strip().upper()[0]
print(resp)
for c in range(0,10,1):
    print(c)

sacar = int(input("Quanto você deseja sacar? "))

while True:
    nota50 = sacar / 50
    nota50 = math.floor(nota50)

    if nota50 >= 1:
        print(f"Total de {nota50} notas de R$50. ")
        sacar = sacar - (nota50 * 50)

    nota20 = sacar / 20
    nota20 = math.floor(nota20)

    if nota20 >= 1:
        print(f"Total de {nota20} notas de R$20. ")
        sacar = sacar - (nota20 * 20)

    nota10 = sacar / 10
    nota10 = math.floor(nota10)

    if nota10 >= 1:
        print(f"Total de {nota10} notas de R$10. ")
        sacar = sacar - (nota10 * 10)

    nota1 = sacar
    if nota1 >= 1:
        print(f"Total de {nota1} notas de R$1. ")
        sacar = sacar - nota1

    if sacar == 0:
        break


maiorPreco = menorPreco = maiorMil = soma = 0
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: R$"))
    if preco > maiorPreco:
        maiorPreco = preco
    if preco > 1000:
        maiorMil += 1
    soma += preco
    if menorPreco > preco or menorPreco == 0:
        nomedoBarato = nome
    opcao = str(input("Você ira continuar cadastrando produtos? 'S/N' ")).upper()
    if opcao == "N":
        break
    elif opcao == "S":
        continue


print(f"O maior preço de produto foi R${maiorPreco} e {maiorMil} produtos custam mais do que R$1000 e o produto mais barato chama {nomedoBarato}")




contadorMaior = contadorHomem = contadorMulher = contadorVoltas = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: 'M/F' ")).upper()
    if idade > 18:
        contadorMaior += 1
    if sexo == "M":
        contadorHomem += 1
    if sexo == "F" and idade < 20:
        contadorMulher += 1
    contadorVoltas += 1
    deseja = str(input("Deseja continuar? 'S/N' ")).upper()
    if deseja == 'N':
        print(f"Existem {contadorMaior} pessoas maiores que 18 anos. {contadorHomem} homens Foram cadastrados e {contadorMulher} mulheres tem menos de 20 anos.")
        break
    elif deseja == 'S':
        continue
    else:
        print("Digite uma opção valida.")

vitorias = 0
print("=-=-=-=-=-=-=-=-=-=-=-=-")
print("Vamos jogar par ou ímpar")
print("=-=-=-=-=-=-=-=-=-=-=-=-")
while True:
    escolha = int(input("Digite o numero desejado: "))
    parImpar = str(input("Par ou ímpar? 'P/I' ")).upper()
    aleatorio = random.randint(0, 20)
    soma = escolha + aleatorio
    if soma % 2 and parImpar == "P":
        vitorias += 1
        print(f"Muito bem você ganhou esta rodada, você jogou {escolha} e o computador {aleatorio}. No total de {soma} que é par")
    elif (soma % 2) != 0 and parImpar == "I":
        print(f"Muito bem você ganhou esta rodada, você jogou {escolha} e o computador {aleatorio}. No total de {soma} que é impar")
        vitorias += 1
    else:
        print(f"Você perdeu! O computador jogou {aleatorio} e você {escolha} no total de {soma}.")
        print(f"Você venceu o total de {vitorias}")
        break

contador = 0

while True:
    n1 = int(input("Digite um numero caso ele seja negativo o programa ira parar: "))
    contador = 0
    if n1 > 0:
        print("_______________________")
        while True:
            contador += 1
            print(f"{n1} x {contador} = {n1 * contador}")
            if contador >= 10:
                print("______________________")
                break
    else:
        break


soma = controle = 0

while True:
    n1 = int(input("Digite aqui um numero ou digite 999 para parar: "))
    if n1 != 999:
        soma += n1
        controle += 1
    else:
        break
print(f"A soma dos numeros é: {soma} e foram digitados: {controle} numeros")
