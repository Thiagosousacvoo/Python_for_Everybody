menor = None
print('Antes')
for value in [9, 41, 12, 3, 74, 15]:
    if menor is None: 
        menor = value
    elif value < menor:
        menor = value
    print(menor, value)
print('Depois', menor)