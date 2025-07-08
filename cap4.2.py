def saudacao(pais):
    if pais == 'br':
        print('Olá')
    elif pais == 'us':
        print('Hello')
    else:
        print('Bonjour')



saudacao('br')
saudacao('us')
saudacao('fr')

print('\n' + '-' * 30 + '\n')

def saudacao(pais):
    if pais == 'br':
        return 'Olá'
    elif pais == 'us':
        return 'Hello'
    else:
        return 'Bonjour'
    


print(saudacao('br'), 'Thiago')
print(saudacao('us'), 'James')
print(saudacao('fr'), 'Mario')


print('\n' + '-' * 30 + '\n') 