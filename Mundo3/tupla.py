import random
c = 0
tuplaPalavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
                'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
aeiou = []
while c < len(tuplaPalavra):
    palavra = tuplaPalavra[c]

    for d in range(0, len(palavra), 1):
        if palavra[d] == 'A' or palavra[d] == 'E' or palavra[d] == 'I' or palavra[d] == 'O' or palavra[d] == 'U':

            aeiou.append(palavra[d])

    print(f'Na palavra {palavra} temos {aeiou}')
    aeiou = []
    c += 1


c = 0
produtoPreco = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
                'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
while c < len(produtoPreco) - 1:
    if c == 0:
        nome = produtoPreco[c]
        c += 1
        print(f'{nome} {"." * (20 - len(nome))}R$ {produtoPreco[c]:.2f}')
    c += 1
    nome = produtoPreco[c]
    c +=1
    print(f'{nome} {"." * (20 - len(nome))}R$ {produtoPreco[c]:.2f}')




listaPar = []
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))

tuplaOrdem = (a, b, c, d)
if tuplaOrdem.count(9) >= 1:
    print(f'O numero 9 apareceu {tuplaOrdem.count(9)} vezes')
else:
    print(f'O numero 9 não apareceu na tupla.')
if tuplaOrdem.count(3) >= 1:
    print(f'A primeira posição em que o numero 3 foi digita é: {tuplaOrdem.index(3) + 1}')
else:
    print(f'O numero 3 não foi digitado na tupla.')

for contador in tuplaOrdem:
    if contador % 2 == 0:
        listaPar.append(contador)

print(f'Os numeros pares foram {listaPar}')

a = random.randint(0, 9999)
b = random.randint(0, 9999)
c = random.randint(0, 9999)
d = random.randint(0, 9999)
e = random.randint(0, 9999)

tupla = (a,b,c,d,e)

print(f'Os números gerados foram: {tupla}')

tupla = sorted(tupla)

print(f'O menor numero da tupla é: {tupla[0]} e o maior numero da tupla é: {tupla[-1]}')


while True:
    brasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
                   'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
                   'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceara SC', 'Cruzeiro', 'CSA',
                   'Chapecoense', 'Avaí')
    for contador, c in enumerate(brasileirao) :
        if contador < 5:
            print(f'O {contador +1}º colocado no Brasileirão 2019 é: {c} ')

    for c in range(16,20,1):
        print(f'O {c+1}º colocado no Brasileirão 2019 é: {brasileirao[c]}')

    print(sorted(brasileirao))

    print(f'O time Chapecoense esta na posição: {brasileirao.index("Chapecoense")} no Brasileirão')

    break

while True:
    extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
               'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

    n1 = int(input('Digite o numero que deseja saber por extenso: '))
    if n1 > 20 or n1 < 0:
        print("Tente um numero entre 0 e 20")
        continue
    print(f'Você digite o número: {extenso[n1]}')