entrada = input("Digite um número: ")
try:
    numero = int(entrada)
except:
    numero = -1

if numero > 0:
    print("Bom trabalho")
else:
    print("Não é um numero")