import random
import math
escolha = ""
controle = 0
n2 = 0
media = 0
while True:
    n1 = int(input("Digite um numero: "))
    escolha = str(input("Você quer digitar outro numero? S/N ")).upper()

    if escolha == "S":
        n2 += n1
        controle += 1
        continue
    elif escolha == "N":
        n2 += n1
        media = n2 / controle
        break
    else:
        print("Escolha uma alternativa valida")
        continue
print(f"A soma dos numeros é {n2} e a média deles é {media}")


controle = int(input("Digite quantos numeros da sequencia de fibonacci você deseja ver: "))
contador = 0
fibonacci = 0
while contador < controle - 1:

    if fibonacci == 0:
        print(fibonacci)
        fibonacci += 1

    elif fibonacci == 1:
        print(fibonacci)
        fibonacci2 = fibonacci
        print(fibonacci)
        fibonacci = fibonacci + fibonacci2
    else:
        print(fibonacci)
        imitador = fibonacci
        fibonacci = fibonacci + fibonacci2
        fibonacci2 = imitador

    contador += 1






aleatorio = 1
controle = int(input("Quantos termos você gostara de ver na PA? ")) + 1
soma = 0
primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))

while True:
    print(primeiroTermo)
    primeiroTermo += razao
    aleatorio += 1
    if aleatorio == controle:
        controle = int(input("Digite mais quantos termos você deseja ver: ")) + 1
        aleatorio = 1
        if controle == 1:
            break



controle = 1
soma = 0
primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
while True:
    print(primeiroTermo)
    primeiroTermo += razao
    controle += 1
    if controle > 10:
        break


x = random.randint(0,10)
tentativas = 0
fatorial = int(input("Digite o valor que você deseja saber o fatorial: "))
controle = fatorial
info = fatorial
print(math.factorial(fatorial))
while fatorial > 1:
    fatorial -= 1
    controle = controle * fatorial
print(f"O valor fatorial do numero {info} é {controle}")


while True:
    opcao = int(input("Digite 1 para adicação 2 para multiplicação 3 para saber o maior 4 para novos numeros ou 5 para sair: "))


    if opcao == 1:
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        print(f" {n1} + {n2} = {n1 + n2}")
    elif opcao == 2:
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        print(f"{n1} x {n2} = {n1 * n2}")
    elif opcao == 3:
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print(f"Os numeros {n1} e {n2} são iguais")
    elif opcao == 4:
        continue
    elif opcao == 5:
        break
    else:
        print(f"A opção {opcao} não é valida, por favor digite uma opção valida.")
while True:
    y = int(input("Digite o numero que você acha que estou pensando: "))
    if y == x:
        print(f"Parabens você acertou o numero em que eu estava pensando em {tentativas + 1} tentativas.")
        break
    else:
        tentativas += 1

while True:
    sexo = str(input("Digite o seu sexo com M ou F: ")).upper()

    if sexo == 'M' or sexo == 'F':
        print(f"Muito bem você digitou sexo corretamente que é: {sexo}.")
        break

print("Fim do programa")