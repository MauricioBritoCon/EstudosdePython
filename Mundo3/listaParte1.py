print
lista80 = []

while True:
    valor = int(input('Digite o valor que deseja adicionar a lista: '))
    lista80.insert(valor, valor)
    continuar = str(input('Deseja adicionar outro numero? S/N ')).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        while True:
            print('Digite uma opção valida. ')
            continuar = str(input('Deseja adicionar outro numero? S/N ')).upper()
            if continuar == 'S' or continuar == 'N':
                break
            else:
                continue

print(lista80)

lista = []

quantidade = int(input('Digite a quantidade de numero que deseja adicionar a lista: '))

for c in range(0,quantidade,1):
    adicionar = int(input('Digite o valor que deseja adicionar a lista: '))

    if adicionar in lista:
        print('Valor não adicionado pois esta duplicado.')
        continue
    else:
        lista.append(adicionar)
        print('Valor adicionado com sucesso.')

print(f'Os numeros digitados não repetidos em ordem crescente são: {sorted(lista)}')

"""Exercicio 78 pulada"""