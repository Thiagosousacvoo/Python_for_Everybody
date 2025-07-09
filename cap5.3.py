iniciando = -1
print('Antes', iniciando)
for numero in [9, 41, 12, 3, 74, 15]:
    if numero > iniciando :
        iniciando = numero
    print(iniciando, numero)

print('Depois', iniciando)