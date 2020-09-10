'''2- Faça um programa que receba o nome, o ano de nascimento de uma pessoa e o ano atual, e mostre uma mensagem com o nome, a idade dessa pessoa e quantos anos ela terá em 2050.
'''


nascimento = int(input('Digite o ano de seu nascimento: '))
nome = str(input('Digite seu nome: '))

print(f'Olá {nome}, sua idade atual é: {2020 - nascimento} e sua idade em 2050 sera {2050 - nascimento}.')

