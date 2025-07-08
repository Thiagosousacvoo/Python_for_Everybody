hora = input("Digite horas: ")
h = float(hora)
valor = input("Digite o valor: ")
v = float(valor)
if h <= 40:
    print(h * v)
else:
    print((40 * v) + ((h - 40) * (v * 1.5)))