
frase = str(input("Digite uma frase: ")).lower()
frase = frase.strip()
print(f"A letra 'a' aparece {frase.count('a')}")
print(f"A primeira vez que o 'a' apareceu foi {frase.find('a')+1}")
print(f"A ultima vez que 'a' apareceu foi {frase.rfind('a')+1}")



import math

nomeCompleto = input("Digite seu nome completo: ")
nomeCompleto = nomeCompleto.split()
print(f"Seu primeiro nome é {nomeCompleto[0]} e seu ultimo nome é {nomeCompleto[-1]}")

frase = input("Digite sua frase: ")
frase = frase.lower()
print("Existem " + frase.count('a') + " 'a' na sua frase. ")
print("Nas posições")



nome = input("Digite seu nome: ")
nome = nome.upper()

if ("SILVA" in nome):
    print("Tem silva no seu nome")
else:
    print("Não tem silva no seu nome")

cidade = input("Digite o nome da sua cidade: ")
cidade = cidade.upper()
cidade = cidade.split()
if cidade[0] == "SANTO":
    print("Sua cidade começa com SANTO")
else:
    print("Sua cidade nao começa com SANTO")
num = input("Digite um numero: ")
num = int(num)
if (num / 1000) > 0:
    milhar = num / 1000
    milhar = math.floor(milhar)
    print(f"Milhar = {milhar}")
    num = num - milhar * 1000
if (num / 100) > 0:
    centena = num  / 100
    centena = math.floor(centena)
    print(f"Centena = {centena}")
    num = num - centena * 100
if (num / 10) > 0:
    dezena = num / 10
    dezena = math.floor(dezena)
    print(f"Dezena = {dezena}")
    num = num - dezena * 10
if (num / 1) > 0:
    print(f"Unidade = {num}")



x = input("Escreva seu nome completo: ")
print(x.upper())
print(x.lower())
print(len(x.strip()))
print(len(x.split()[1]))

