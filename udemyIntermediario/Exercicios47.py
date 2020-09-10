lista = [1, 2, 3, 4, 5]

print(*lista)


def fizzbuzz(n1):

    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'FizzBuzz'
    elif n1 % 5 == 0:
        return 'Buzz'
    elif n1 % 3 == 0:
        return 'Fizz'
    else:
        return n1


chama = fizzbuzz(int(input('Digite o valor que deseja saber o fizzbuzz: ')))

print(chama)

def porcentagem(n1, n2):
    return n1 + ((n2 / 100) * n1)


chama = porcentagem(float(input('Digite o valor desejado: ')),
                    float(input('Digite a porcentagem adicional: ')))
print(chama)


def soma(n1, n2, n3):
    return n1 + n2 + n3


chama = soma(int(input('Digite o primeiro numero: ')),
             int(input('Digite o segundo numero: ')),
             int(input('digite o terceiro numero: ')))
print(chama)


def saudacao(msg, nome):
    print(msg, nome)


saudacao('Ola', 'mundo')
