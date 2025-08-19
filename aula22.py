# OPERADOR LÓGICO OR

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')

    """
    a expressão acima da certo mas, sempre que houver or e and na mesma expressão, ela pode ser ambigua

    se vc colocar engre parentes a primeira condição a ser avaliada, melhora a condição

    """

# Avaliação de curto circuito com o OR

# print(0 or False or 0 or 'abc')

# ele vai retornar o primeiro valor verdadeiro, no caso da expressão acima o abc
