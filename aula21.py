"""
Aula de Operadores Lógicos

and (e)
or (ou)
not (nâo)

"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')