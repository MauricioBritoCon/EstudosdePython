import time
import datetime
anoatual = datetime.datetime.now()
n = 0
m = 0
o = 0
p = ""
q = 0
r = 0
t = 0
u = 0
idadeMedia = 0
nomeVelho = ''
idadeVelha = 0
mulherNova = 0

for c in range(0, 4, 1):
    nome = str(input("Digite seu nome"))
    sexo = str(input("Digite se é do sexo 'masculino' ou 'feminino'"))
    idade = int(input("Digite sua idade"))

    idadeMedia += idade
    if sexo == 'masculino' and idade > idadeVelha:
        idadeVelha = idade
        nomeVelho = nome

    if sexo == 'feminino' and idade < 20:
        mulherNova += 1

print(f"O numero de mulheres com menos de 20 anos é {mulherNova}")
print(f"O nome do homem mais velho é: {nomeVelho} e sua idade é de {idadeVelha}")
print(f"A idade média é: {idadeMedia /  4}")


for c in range(0, 5, 1):
    peso = float(input("Digite o peso em kg: "))

    if peso > t:
        t = peso
    elif peso < u or u == 0:
        u = peso

print(f"O maior peso foi de {t}kg e o menor peso foi de {u}kg.")


for c in range(0,7,1):
    ano = int(input("Digite o ano de nascimento: "))
    if anoatual.year - ano >= 21:
        q += 1
    else:
        r += 1

print(f"O numero de pessoas maior de idade é {q} e o numero de pessoas menor de idade é {r}")



palavra = str(input("Digite a frase que você quer descobrir se é um palindromo: "))
palavra = palavra.replace(" ", "")

for c in range(len(palavra) -1, -1, -1):
    p += palavra[c]
print(p)

if p == palavra:
    print(f"{palavra} é um palindromo")
else:
    print(f"{palavra} não é um palindromo")

numeroPrimo = int(input("Digite o numero que deseja saber se é primo: "))

for c in range(1, numeroPrimo, 1):
    if numeroPrimo % c == 0:
        o += 1
if o == 1:
    print(f"O numero {numeroPrimo} é primo")
else:
    print(f"O numero {numeroPrimo} não é primo")

primeiroTermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))

for c in range(1,11,1):

    print(primeiroTermo)
    primeiroTermo += razao


for c in range(1,7,1):
    numero = int(input("Digite o numero que caso par seja somado e impar sera desconsiderado: "))
    if numero % 2 == 0:
        m += numero
print(m)
tabuada = int(input("Escolha o numero que deseja ver a tabuada: "))

for c in range(1,11,1):
    print(f"{tabuada} x {c} = {tabuada * c}")

for c in range(1,500,1):
    if c % 3 == 0:
        n += c
print(n)
for c in range(1,51,1):
    if c % 2 == 0:
        print(c)


for c in range(10,-1,-1):
    time.sleep(1)
    print(c)
print("KABUUMM FOGOS")
