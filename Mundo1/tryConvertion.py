def converter_valor(variavel):
    try:
        variavel = int(variavel)
        return variavel
    except ValueError:
        try:
            variavel = float(variavel)
            return variavel
        except ValueError:
            pass

while True:
    a = converter_valor(input("Digite o valor:"))

    if a == 0:
        print("Todo numero multiplicado por 0 é 0 irmão")
    elif a is not None:
        print(f"{a * 10}\n")
    else:
        print("O programa deu pau irmao\n")
